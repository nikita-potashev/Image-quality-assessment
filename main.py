import glob

import numpy as np
from keras.models import model_from_json

from model import models, preproc


def load_model(arch, weights):
    topology = open(arch, "r")
    topology = topology.read()
    model = model_from_json(topology)
    model.load_weights(weights)

    return model


def voting_predict():
    blur_model = load_model('model/json/arch/blur.json',
                            'model/weights/blur.h5')
    noise_model = load_model(
        'model/json/arch/noise.json', 'model/weights/noise.h5')

    data = glob.glob('/home/nick/Desktop/predict/blur/*')

    blurred = preproc.load_imgs(data, (500, 500, 1), 'grayscale')

    score1 = blur_model.predict_classes(
        preproc.load_imgs(data, (250, 250, 1), 'grayscale'))
    score2 = noise_model.predict_classes(blurred)
    print(score1)
    print(score2)
    temp = []
    for string in data:
        temp.append(preproc.read_img(string, (500, 500, 3), color_mode='rgb'))

    score3 = []
    for item in temp:
        score3.append(models.bright_model(item))

    print(score3)


if __name__ == "__main__":
    # json_file = open("model/json/arch/blur.json", "r")
    # loaded_model_json = json_file.read()
    # json_file.close()

    # model = model_from_json(loaded_model_json)

    # model.load_weights("model/weights/blur.h5")

    # data = glob.glob('/home/nick/Desktop/predict/blur/*')

    # blurred = preproc.load_imgs(data,(250,250,1),'grayscale')

    # score = model.predict_classes(blurred)
    # print(score)
    voting_predict()
