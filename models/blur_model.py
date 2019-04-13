import os

import numpy as np
from tensorflow.python.keras.layers import (BatchNormalization, Conv2D, Dense,
                                            Dropout, Flatten, MaxPool2D,
                                            MaxPooling2D)
from tensorflow.python.keras.models import Model, Sequential

from base.base_model import BaseModel


class BlurModel(BaseModel):
    def __init__(self, config):
        super(BlurModel, self).__init__(config)

    @classmethod
    def build_model(self, config):
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
