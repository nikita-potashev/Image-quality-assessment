import os

import matplotlib.pyplot as plt
from tensorflow.python.keras.callbacks import ModelCheckpoint, TensorBoard
from tensorflow.python.keras.callbacks import LearningRateScheduler, ReduceLROnPlateau
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from base.base_ensemble_train import BaseEnsembleTrain


class BlurEnsembleTrainer(BaseEnsembleTrain):
    def __init__(self, models, data_train, data_test, config):
        super(BlurEnsembleTrainer, self).__init__(models, data_train, data_test, config)  # models - list of models
        # self.callbacks = []
        # self.loss = []
        # self.acc = []
        # self.val_loss = []
        # self.val_acc = []
        # self.init_saver()

    # def init_saver(self):
    #     self.callbacks.append(
    #         ModelCheckpoint(
    #             filepath=os.path.join(
    #                 self.config.checkpoint_dir, '%s-{epoch:02d}-{val_loss:.2f}.hdf5' % self.config.exp_name),
    #             monitor='val_loss',
    #             mode='min',
    #             save_best_only=True,
    #             save_weights_only=True,
    #             verbose=True,
    #         )
    #     )

    #     self.callbacks.append(
    #         TensorBoard(
    #             log_dir=self.config.summary_dir,
    #             write_graph=True,
    #         )
    #     )

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
    # history = self.model.fit(
    #     self.data[0], self.data[1],
    #     epochs=self.config.num_epochs,
    #     verbose=True,
    #     batch_size=self.config.batch_size,
    #     validation_split=self.config.validation_split,
    #     callbacks=self.callbacks,
    # )
    # self.loss.extend(history.history['loss'])
    # self.acc.extend(history.history['acc'])
    # self.val_loss.extend(history.history['val_loss'])
    # self.val_acc.extend(history.history['val_acc'])

    # def visualize(self):
    #     plt.plot(self.loss, 'b', label = 'loss')
    #     plt.plot(self.val_loss, 'r', label = 'val_loss')
    #     plt.savefig(os.path.join(self.config.visual_dir, '{}.pdf'.format(self.config.exp_name)))
