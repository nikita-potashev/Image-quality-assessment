import os

import matplotlib.pyplot as plt
from tensorflow.python.keras.callbacks import ModelCheckpoint, TensorBoard

from base.base_train import BaseTrain


class BlurModelTrainer(BaseTrain):
    def __init__(self, model, data, config):
        super(BlurModelTrainer, self).__init__(model, data, config)
        self.callbacks = []
        self.loss = []
        self.acc = []
        self.val_loss = []
        self.val_acc = []
        self.init_saver()

    def init_saver(self):
        self.callbacks.append(
            ModelCheckpoint(
                filepath=os.path.join(
                    self.config.checkpoint_dir, '%s-{epoch:02d}-{val_loss:.2f}.hdf5' % self.config.exp_name),
                monitor='val_loss',
                mode='min',
                save_best_only=True,
                save_weights_only=True,
                verbose=True,
            )
        )

        self.callbacks.append(
            TensorBoard(
                log_dir=self.config.summary_dir,
                write_graph=True,
            )
        )

    def train(self):
        history = self.model.fit(
            self.data[0], self.data[1],
            epochs=self.config.num_epochs,
            verbose=True,
            batch_size=self.config.batch_size,
            validation_split=self.config.validation_split,
            callbacks=self.callbacks,
        )
        self.loss.extend(history.history['loss'])
        self.acc.extend(history.history['acc'])
        self.val_loss.extend(history.history['val_loss'])
        self.val_acc.extend(history.history['val_acc'])

    def visualize(self):
        plt.plot(self.loss, 'b', label = 'loss')
        plt.plot(self.val_loss, 'r', label = 'val_loss')
        plt.savefig(os.path.join(self.config.visual_dir, '{}.pdf'.format(self.config.exp_name)))
