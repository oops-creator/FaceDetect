import cv2
import keras
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import numpy as np
from PIL import Image
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img
import ModelClass
import os


class Recognize:

    def __init__(self):
        self.epsilon = 0.40 
        self.vggFace = ModelClass.Models()
        self.vggFace = self.vggFace.getModel()

    def normalize(self,img):
        norm_image = cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        return norm_image

    def preprocess(self,image_path):
        img = load_img(image_path, target_size=(224, 224))
        img = img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = self.normalize(img)
        return img

    def preprocessnp(self,imagearr):
        img = cv2.cvtColor(imagearr, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = img.resize((224,224))
        img = img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = self.normalize(img)
        return img

    def findCosineDistance(self,source_representation, test_representation):
        a = np.matmul(np.transpose(source_representation), test_representation)
        b = np.sum(np.multiply(source_representation, source_representation))
        c = np.sum(np.multiply(test_representation, test_representation))
        return 1 - (a / (np.sqrt(b) * np.sqrt(c)))

    def findEuclideanDistance(self,source_representation, test_representation):
        euclidean_distance = source_representation - test_representation
        euclidean_distance = np.sum(np.multiply(euclidean_distance, euclidean_distance))
        euclidean_distance = np.sqrt(euclidean_distance)
        return euclidean_distance

    
 
    def verifyFace2(self,img1, img2):
        img1_representation = self.vggFace.predict(self.preprocessnp(img1))[0,:]
        img2_representation = self.vggFace.predict(self.preprocess(img2))[0,:]
 
        cosine_similarity = self.findCosineDistance(img1_representation, img2_representation)
        euclidean_distance = self.findEuclideanDistance(img1_representation, img2_representation)
 
        if(cosine_similarity < self.epsilon):
            print("Found a match")
            cv2.namedWindow('match',cv2.WINDOW_NORMAL)
            cv2.resizeWindow('match', 600,600)
            match = cv2.imread(img2)
            cv2.imshow('match',match)
            cv2.waitKey()
            cv2.destroyAllWindows() 
            return True
        else:
            return False

 

    
    def recognize(self,imgpath):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        img = cv2.imread(imgpath)
        gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)
        (x, y, w, h) = faces[0]
        img = self.preprocessnp(img[y:y+h,x:x+w])
        directory = os.path.join(os.curdir,'database')
        files = os.listdir(directory)
        for i in files:
            check = self.verifyFace2(img , os.path.join(directory , i))
            if check:
                break
    
        

        
        