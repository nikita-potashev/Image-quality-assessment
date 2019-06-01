import glob
import os
import tensorflow as tf
from gui.prediction import Prediction

import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

#
from sklearn import svm, datasets
import numpy as np
import matplotlib.pyplot as plt
from data_loader.data_loader import read_img


class Signals(QObject):
    def __init__(self):
        QObject.__init__(self)

    @pyqtSlot()
    def init_models(self):
        print('Creating prediction models..')

        models = {
            'experiments/json/blur/blur1.json': 'experiments/blur_model1/checkpoint/blur_model1-08-0.11.h5',
            'experiments/json/blur/blur2.json': 'experiments/blur_model2/checkpoint/blur_model2-01-0.05.h5',
            'experiments/json/blur/blur3.json': 'experiments/blur_model3/checkpoint/blur_model3-12-0.06.h5',

            'experiments/json/noise/noise1.json': 'experiments/noise_model1/checkpoint/model1-19-0.35.h5',
            'experiments/json/noise/noise2.json': 'experiments/noise_model2/checkpoint/model2-18-0.30.h5',
            'experiments/json/noise/noise3.json': 'experiments/noise_model3/checkpoint/model3-94-0.13.h5'


        }

        self.pred = Prediction(models)

    @pyqtSlot(str, result=str)
    def prediction(self, arg1):
        self.pred.predictions = {}
        self.pred.predict_class(arg1)
        # print(self.pred.predictions)
        # print(type(self.pred.predictions.values()))
        # return str(list(self.pred.predictions.values())[-1])
        print(self.pred.predictions)
        return str(self.pred.predictions.values())


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"
    engine = QQmlApplicationEngine()

    signals = Signals()
    engine.rootContext().setContextProperty("signals", signals)
    engine.load(QUrl("gui/ui.qml"))

    if not engine.rootObjects():
        sys.exit(-1)

    engine.quit.connect(app.quit)
    sys.exit(app.exec_())


