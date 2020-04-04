
from tensorflow.keras import Sequential
from tensorflow.keras.models import load_model
from tensorflow.python.keras.layers import Convolution2D, ZeroPadding2D
from tensorflow.python.keras.layers import MaxPooling2D, Activation
from tensorflow.python.keras.layers import Flatten, Dropout
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.models import model_from_json
from tensorflow.python.keras.models import Model
import os
import h5py


class Models:
    def __init__(self):
        model_dir = os.path.join(os.getcwd(), 'mobileNet.h5')
        self.model = load_model(model_dir  ,compile=False)
    def getModel(self):
        mobNet = Model(inputs=self.model.layers[0].input, outputs=self.model.layers[-2].output)
        return mobNet
