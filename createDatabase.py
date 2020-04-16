import os
import cv2
import random

if __name__ == "__main__":
    toDatabase = './imagesForDatabase'
    database = './database'
    face_cascade = cv2.CascadeClassifier(
        'haarcascade_frontalface_default.xml')
    for i in os.listdir(toDatabase):
        print(f'Processing image {i}')
        img = cv2.imread(os.path.join(toDatabase , i))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)
        (x, y, w, h) = faces[0]
        img = img[y:y+h, x:x+w]
        filename = os.path.join(database ,str(hex(hash(random.random())))[2:] + '.jpeg')
        cv2.imwrite(filename, img)



