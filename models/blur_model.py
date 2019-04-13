import os

import numpy as np
from tensorflow.python.keras.layers import (BatchNormalization, Conv2D, Dense,
                                            Dropout, Flatten, MaxPool2D,
                                            MaxPooling2D, AveragePooling2D)
from tensorflow.python.keras.models import Model, Sequential

from base.base_model import BaseModel


class BlurModel(BaseModel):
    def __init__(self, config):
        super(BlurModel, self).__init__(config)

    @classmethod
    def build_model1(self, config):
        self.model = Sequential()
        self.model.add(Conv2D(8, (5, 5), activation='relu', input_shape=(500, 500, 1)))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.2))
        self.model.add(Conv2D(16, (3, 3), activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.2))

        self.model.add(Flatten())
        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(16, activation='relu'))
        self.model.add(Dropout(0.3))

        self.model.add(Dense(2, activation='sigmoid'))

        self.model.compile(loss='binary_crossentropy',
                           optimizer=config.optimizer,
                           metrics=['accuracy'])
        return self.model
    
    @classmethod
    def build_model2(self, config):
        self.model = Sequential()
        self.model.add(Conv2D(6, kernel_size=(5, 5), strides=(1, 1), activation='relu', input_shape=(500,500,1), padding="same"))
        self.model.add(AveragePooling2D(pool_size=(2, 2), strides=(1, 1), padding='valid'))
        self.model.add(Conv2D(16, kernel_size=(5, 5), strides=(1, 1), activation='relu', padding='valid'))
        self.model.add(AveragePooling2D(pool_size=(2, 2), strides=(2, 2), padding='valid'))
        self.model.add(Conv2D(120, kernel_size=(5, 5), strides=(1, 1), activation='relu', padding='valid'))
        self.model.add(Flatten())
        self.model.add(Dense(84, activation='relu'))
        self.model.add(Dense(2, activation='sigmoid'))
        self.model.compile(loss='binary_crossentropy',optimizer=config.optimizer,metrics=['accuracy'])
        return self.model

    @classmethod
    def build_model3(self, config):
        self.model = Sequential()
        self.model.add(Conv2D(32, kernel_size = (3,3), activation='relu', input_shape = (500,500,1)))
        self.model.add(BatchNormalization())
        self.model.add(Conv2D(32, kernel_size = (3,3), activation='relu'))
        self.model.add(BatchNormalization())
        self.model.add(Conv2D(32, kernel_size = (5,5), strides=2, padding='same', activation='relu'))
        self.model.add(BatchNormalization())
        self.model.add(Dropout(0.4))
        self.model.add(Conv2D(64, kernel_size = (3,3), activation='relu'))
        self.model.add(BatchNormalization())
        self.model.add(Conv2D(64, kernel_size = (3,3), activation='relu'))
        self.model.add(BatchNormalization())
        self.model.add(Conv2D(64, kernel_size = (5,5), strides=2, padding='same', activation='relu'))
        self.model.add(BatchNormalization())
        self.model.add(Dropout(0.4))
        self.model.add(Conv2D(128, kernel_size = 4, activation='relu'))
        self.model.add(BatchNormalization())

        self.model.add(Flatten())
        self.model.add(Dropout(0.4))

        self.model.add(Dense(2, activation = "sigmoid"))
        self.model.compile(loss='binary_crossentropy',optimizer=config.optimizer,metrics=['accuracy'])
        
        return self.model