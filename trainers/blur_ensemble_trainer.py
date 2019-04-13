import os

import matplotlib.pyplot as plt
from tensorflow.python.keras.callbacks import ModelCheckpoint, TensorBoard
from tensorflow.python.keras.callbacks import LearningRateScheduler, ReduceLROnPlateau
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from base.base_ensemble_train import BaseEnsembleTrain


class BlurEnsembleTrainer(BaseEnsembleTrain):
    def __init__(self, models, data_train, data_test, config):
        super(BlurEnsembleTrainer, self).__init__(models, data_train, data_test, config)  # models - list of models

    def train_gen(self):
        print(len(self.data_test))
        datagen = ImageDataGenerator(rotation_range=10, zoom_range=0.1, width_shift_range=0.1, height_shift_range=0.1)
        datagen.fit(self.data_train[0])
        for i in range(len(self.models)):
            self.models[i].fit_generator(datagen.flow(self.data_train[0], self.data_train[1], batch_size=self.config.batch_size),
                                         epochs=self.config.num_epochs, steps_per_epoch=self.data_train[0].shape[0] // self.config.batch_size,
                                         validation_data=(
                                             self.data_test[0], self.data_test[1]),
                                         callbacks=[ReduceLROnPlateau(
                                             monitor='lr', patience=3, factor=0.1)],
                                         verbose=2)
            self.models.append(self.models[i])
