import glob

import numpy as np
from keras.models import model_from_json

from model import preproc

def voting_predict():
    pass

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
