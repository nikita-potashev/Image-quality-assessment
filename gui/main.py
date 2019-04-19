from models.blur_model import BlurModel
from models.noise_model import NoiseModel
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.models import model_from_json
from data_loader.data_loader import read_img
import numpy as np
import glob


def load_model(json, weights):
    json_file = open(json, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights(weights)
    return loaded_model


def prediction(models_dict, imgs):
    models = []
    for k, v in models_dict.items():
        models.append(load_model(k, v))

    predictions = []
    print(imgs[0])
    for item in imgs:
        pred = []
        for model in models:
            img = read_img(item, (500, 500, 1))
            temp = np.array(img, np.float32)/255.0
            temp = np.expand_dims(temp, axis=0)
            score = model.predict_classes(temp)[0]
            pred.append(score)
        predictions.append(pred)
    return predictions


def app():
    models = {
        'experiments/json/blur/blur1.json': 'experiments/blur_model1/checkpoint/blur_model1-08-0.11.h5',
        'experiments/json/blur/blur2.json': 'experiments/blur_model2/checkpoint/blur_model2-01-0.05.h5',
        'experiments/json/blur/blur3.json': 'experiments/blur_model3/checkpoint/blur_model3-12-0.06.h5'

        # 'models/json/noise/noise1.json': 'experiments/noise_model1/checkpoint/noise_model1-01-7.81.h5',
        # 'models/json/noise/noise2.json': 'experiments/noise_model2/checkpoint/noise_model2-01-8.11.h5',
        # 'models/json/noise/noise3.json': 'experiments/noise_model3/checkpoint/noise_model3-01-9.24.h5'



    }
    data = glob.glob('/home/nick/Desktop/predict/*.jpg')
    print(prediction(models, data))

