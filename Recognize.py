import os
import ModelClass
from tensorflow.keras.preprocessing.image import array_to_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from PIL import Image
import numpy as np
import cv2
import tensorflow.keras as keras
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


class Recognize:

    def __init__(self):
        self.epsilon = .05
        self.mobNet = ModelClass.Models()
        self.mobNet = self.mobNet.getModel()

    def normalize(self, img):
        norm_image = cv2.normalize(
            img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        return norm_image

 

    def preprocessnp(self, imagearr):
        img = cv2.cvtColor(imagearr, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img.astype(np.uint8))
        img = img.resize((224, 224))
        img = img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = self.normalize(img)
        return img

    def preprocess(self, image_path):
        img = cv2.imread(image_path)
        img = self.preprocessnp(img)
        return img

    def findCosineSimilarity(self, source_representation, test_representation):
        a = np.matmul(np.transpose(source_representation), test_representation)
        b = np.sum(np.multiply(source_representation, source_representation))
        c = np.sum(np.multiply(test_representation, test_representation))
        return 1 - (a / (np.sqrt(b) * np.sqrt(c)))

    def findEuclideanDistance(self, source_representation, test_representation):
        euclidean_distance = source_representation - test_representation
        euclidean_distance = np.sum(np.multiply(
            euclidean_distance, euclidean_distance))
        euclidean_distance = np.sqrt(euclidean_distance)
        return euclidean_distance

    def verifyFace2(self, img1, img2url):
        img1_representation = self.mobNet.predict(self.preprocessnp(img1))[0, :]
        img2_representation = self.mobNet.predict(self.preprocess(img2url))[0, :]

        cosine_similarity = self.findCosineSimilarity(
            img1_representation, img2_representation)
        euclidean_distance = self.findEuclideanDistance(
            img1_representation, img2_representation)

        if(cosine_similarity < self.epsilon):
            print("Found a match")
            cv2.namedWindow('match', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('match', 600, 600)
            match = cv2.imread(img2url)
            cv2.imshow('match', match)
            cv2.waitKey()
            cv2.destroyAllWindows()
            return True
        else:
            return False


    def verifyFace(self, img1url, img2url):
        img1_representation = self.mobNet.predict(self.preprocess(img1url))[0, :]
        img2_representation = self.mobNet.predict(self.preprocess(img2url))[0, :]

        cosine_similarity = self.findCosineSimilarity(
            img1_representation, img2_representation)
        euclidean_distance = self.findEuclideanDistance(
            img1_representation, img2_representation)

        if(cosine_similarity < self.epsilon):
            return img2url
        else:
            return None


    def recognize(self, imgpath):
        face_cascade = cv2.CascadeClassifier(
            'haarcascade_frontalface_default.xml')
        img = cv2.imread(imgpath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)
        (x, y, w, h) = faces[0]
        img = self.preprocessnp(img[y:y+h, x:x+w])
        directory = os.path.join(os.getcwd(), 'database')
        files = os.listdir(directory)
        for i in files:
            print(i)
            check = self.verifyFace2(img, os.path.join(directory, i))
            if check:
                print('founf f')
                break
