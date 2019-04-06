import os

import numpy as np
from tensorflow.python.keras.layers import (Conv2D, Dense, Dropout, Flatten,
                                            MaxPool2D, MaxPooling2D)
from tensorflow.python.keras.models import Model, Sequential

from base.base_model import BaseModel


class NoiseModel(BaseModel):
    def __init__(self, config):
        super(NoiseModel, self).__init__(config)
        self.build_model()

    def build_model(self):
        self.model = Sequential()
        self.model.add(Conv2D(4, (3, 3), activation='relu',
                              input_shape=(500, 500, 1)))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.2))
        self.model.add(Conv2D(8, (5, 5), activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.2))

        self.model.add(Flatten())
        self.model.add(Dense(16, activation='relu'))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(2, activation='sigmoid'))

        self.model.compile(loss='binary_crossentropy',
                           optimizer=self.config.optimizer,
                           metrics=['accuracy'])
