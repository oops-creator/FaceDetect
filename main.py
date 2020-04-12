#Populate 'database'  folder with the dataset of images to be recognize from 

import Recognize

recognizer = Recognize.Recognize()

#recognize takes path to the image to be recognized
recognizer.recognize('011.jpg')
