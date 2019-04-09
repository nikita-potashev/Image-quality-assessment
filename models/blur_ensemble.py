import os

import numpy as np
from tensorflow.python.keras.layers import (BatchNormalization, Conv2D, Dense,
                                            Dropout, Flatten, MaxPool2D,
                                            MaxPooling2D)
from tensorflow.python.keras.models import Model, Sequential

from base.base_model import BaseModel


class BlurEnsemble(BaseModel):
    def __init__(self, config):
        super(BlurEnsemble, self).__init__(config)
        self.models = []
        self.build_model_batch_norm()
        self.build_model_high_drop()
        self.build_model_low_drop()

    def build_model_batch_norm(self):
        model = Sequential()
        model.add(
            Conv2D(8, (3, 3), activation='relu', input_shape=(500, 500, 1)))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(BatchNormalization())
        model.add(Flatten())
        model.add(Dense(10, activation='relu'))
        model.add(BatchNormalization())
        model.add(Dense(2, activation='sigmoid'))

        model.compile(loss='binary_crossentropy',
                      optimizer=self.config.optimizer,
                      metrics=['accuracy'])

        self.models.append(model)

    def build_model_high_drop(self):
        model = Sequential()
        model.add(
            Conv2D(6, (3, 3), activation='relu', input_shape=(500, 500, 1)))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.35))
        model.add(Flatten())
        model.add(Dense(8, activation='relu'))
        model.add(Dropout(0.2))
        model.add(Dense(2, activation='sigmoid'))

        model.compile(loss='binary_crossentropy',
                      optimizer=self.config.optimizer,
                      metrics=['accuracy'])
        self.models.append(model)

    def build_model_low_drop(self):
        model = Sequential()
        model.add(
            Conv2D(5, (3, 3), activation='relu', input_shape=(500, 500, 1)))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.5))
        model.add(Flatten())
        model.add(Dense(32, activation='relu'))
        model.add(Dropout(0.2))
        model.add(Dense(16, activation='relu'))
        model.add(Dropout(0.2))
        model.add(Dense(2, activation='sigmoid'))

        model.compile(loss='binary_crossentropy',
                      optimizer=self.config.optimizer,
                      metrics=['accuracy'])
        self.models.append(model)
