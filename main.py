# import glob
import os
import tensorflow as tf
from gui.prediction import Prediction

import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class Signals(QObject):
    def __init__(self):
        QObject.__init__(self)

    prediction_result = pyqtSignal(dict, arguments=['prediction'])

    @pyqtSlot(str)
    def prediction(self, arg1):
        print('Creating prediction models..')

        models = {
            'experiments/json/blur/blur1.json': 'experiments/blur_model1/checkpoint/blur_model1-08-0.11.h5',
            'experiments/json/blur/blur2.json': 'experiments/blur_model2/checkpoint/blur_model2-01-0.05.h5',
            'experiments/json/blur/blur3.json': 'experiments/blur_model3/checkpoint/blur_model3-12-0.06.h5',

            'experiments/json/noise/noise1.json': 'experiments/noise_model1/checkpoint/model1-19-0.35.h5',
            'experiments/json/noise/noise2.json': 'experiments/noise_model2/checkpoint/model2-18-0.30.h5',
            'experiments/json/noise/noise3.json': 'experiments/noise_model3/checkpoint/model3-94-0.13.h5'


        }
        arg1 = arg1[7:]
        pred = Prediction(models)
        lst_data = []
        lst_data.append(arg1)
        pred.predict_class(lst_data)
        print(pred.predictions)
        self.prediction_result.emit(pred.predictions)


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


# if __name__ == "__main__":

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# models = {
#     'experiments/json/blur/blur1.json': 'experiments/blur_model1/checkpoint/blur_model1-08-0.11.h5',
#     'experiments/json/blur/blur2.json': 'experiments/blur_model2/checkpoint/blur_model2-01-0.05.h5',
#     'experiments/json/blur/blur3.json': 'experiments/blur_model3/checkpoint/blur_model3-12-0.06.h5',

#     'experiments/json/noise/noise1.json': 'experiments/noise_model1/checkpoint/model1-19-0.35.h5',
#     'experiments/json/noise/noise2.json': 'experiments/noise_model2/checkpoint/model2-18-0.30.h5',
#     'experiments/json/noise/noise3.json': 'experiments/noise_model3/checkpoint/model3-94-0.13.h5'


# }
# data = glob.glob('/home/nick/Desktop/predict/trained/blur/*')

# print('Prediction..')

# pred = Prediction(models)
# pred.predict_class(data)
# print('Save prediction..')
# pred.save_predictions('data.json')
