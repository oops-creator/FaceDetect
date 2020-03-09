
from keras import Sequential
from keras.layers  import Convolution2D , ZeroPadding2D
from keras.layers  import MaxPooling2D , Activation 
from keras.layers  import Flatten , Dropout
from keras.layers  import Dense
from keras.models import model_from_json
from keras.models import Model
import os

class Models:
    

    def __init__(self):
        self.model = Sequential()
        self.model.add(ZeroPadding2D((1, 1), input_shape=(224, 224, 3)))
        self.model.add(Convolution2D(64, (3, 3), activation='relu'))
        self.model.add(ZeroPadding2D((1, 1)))
        self.model.add(Convolution2D(64, (3, 3), activation='relu'))
        self.model.add(MaxPooling2D((2, 2), strides=(2, 2)))

        self.model.add(ZeroPadding2D((1, 1)))
        self.model.add(Convolution2D(128, (3, 3), activation='relu'))
        self.model.add(ZeroPadding2D((1, 1)))
        self.model.add(Convolution2D(128, (3, 3), activation='relu'))
        self.model.add(MaxPooling2D((2, 2), strides=(2, 2)))

        self.model.add(ZeroPadding2D((1, 1)))
        self.model.add(Convolution2D(256, (3, 3), activation='relu'))
        self.model.add(ZeroPadding2D((1, 1)))
        self.model.add(Convolution2D(256, (3, 3), activation='relu'))
        self.model.add(ZeroPadding2D((1, 1)))
        self.model.add(Convolution2D(256, (3, 3), activation='relu'))
        self.model.add(MaxPooling2D((2, 2), strides=(2, 2)))

        self.model.add(ZeroPadding2D((1, 1)))
        self.model.add(Convolution2D(512, (3, 3), activation='relu'))
        self.model.add(ZeroPadding2D((1, 1)))
        self.model.add(Convolution2D(512, (3, 3), activation='relu'))
        self.model.add(ZeroPadding2D((1, 1)))
        self.model.add(Convolution2D(512, (3, 3), activation='relu'))
        self.model.add(MaxPooling2D((2, 2), strides=(2, 2)))

        self.model.add(ZeroPadding2D((1, 1)))
        self.model.add(Convolution2D(512, (3, 3), activation='relu'))
        self.model.add(ZeroPadding2D((1, 1)))
        self.model.add(Convolution2D(512, (3, 3), activation='relu'))
        self.model.add(ZeroPadding2D((1, 1)))
        self.model.add(Convolution2D(512, (3, 3), activation='relu'))
        self.model.add(MaxPooling2D((2, 2), strides=(2, 2)))

        self.model.add(Convolution2D(4096, (7, 7), activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Convolution2D(4096, (1, 1), activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Convolution2D(2622, (1, 1)))
        self.model.add(Flatten())
        self.model.add(Activation('softmax'))
        currentdir = os.path.join(os.curdir,'vgg_face_weights.h5')
        self.model.load_weights(currentdir)


    def getModel(self):
        vggFace = self.model(inputs=self.model.layers[0].input, outputs=self.model.layers[-2].output)
        return vggFace