import json

import numpy as np
from tensorflow.python.keras.models import model_from_json

from data_loader.data_loader import read_img
import time


class Prediction:
    def __init__(self, saved_models):
        self.saved_models = saved_models
        self.models = []
        self.predictions = {}
        self.build_models()

    def build_models(self):
        """
            load keras model from json and h5
        """
        if not self.saved_models:
            raise ValueError

        for key, value in self.saved_models.items():
            json_file = open(key, 'r')
            loaded_model_json = json_file.read()
            json_file.close()
            loaded_model = model_from_json(loaded_model_json)
            loaded_model.load_weights(value)
            self.models.append(loaded_model)

    def predict_class(self, image, input_shape=(500, 500, 1)):

        if not image:
            raise ValueError
        # start_time = time.time()

        predict_vector = []
        subpredict_dict = {}
        for model in self.models:
            temp = read_img(image, input_shape)
            temp = np.array(temp, np.float32)/255.0
            temp = np.expand_dims(temp, axis=0)

            score = model.predict_classes(temp)[0]
            predict_vector.append(int(score))

            subpredict_dict['Blur'] = predict_vector[:3]
            subpredict_dict['Noise'] = predict_vector[3:]

            if predict_vector[:3].count(1) == 3 or predict_vector[3:].count(1) == 3:
                subpredict_dict['TotalPrediction'] = 1
            else:
                subpredict_dict['TotalPrediction'] = max(set(predict_vector), key=predict_vector.count)

        self.predictions[image] = subpredict_dict
        
        # elapsed_time = time.time() - start_time
        # print(elapsed_time)

    def save_predictions(self, path, sort_keys=True):
        with open(path, 'w') as output:
            json.dump(self.predictions, output, sort_keys=sort_keys)
