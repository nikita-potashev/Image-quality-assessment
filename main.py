from gui.main import Prediction
from utils.config import process_config
from utils.utils import get_args
import glob
import os
import tensorflow as tf

if __name__ == "__main__":

    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
    models = {
        'experiments/json/blur/blur1.json': 'experiments/blur_model1/checkpoint/blur_model1-08-0.11.h5',
        'experiments/json/blur/blur2.json': 'experiments/blur_model2/checkpoint/blur_model2-01-0.05.h5',
        'experiments/json/blur/blur3.json': 'experiments/blur_model3/checkpoint/blur_model3-12-0.06.h5',

        'experiments/json/noise/noise1.json': 'experiments/noise_model1/checkpoint/model1-19-0.35.h5',
        'experiments/json/noise/noise2.json': 'experiments/noise_model2/checkpoint/model2-18-0.30.h5',
        'experiments/json/noise/noise3.json': 'experiments/noise_model3/checkpoint/model3-94-0.13.h5'


    }
    data = glob.glob('/home/nick/Desktop/predict/trained/blur/*')

    print('Prediction..')
    pred = Prediction(models)
    pred.predict_class(data)
    print('Save prediction..')
    pred.save_predictions('data.json')
