import glob

import numpy as np
from keras.models import model_from_json

from model import models, preproc
from sklearn import svm

def load_model(arch, weights):
    topology = open(arch, "r")
    topology = topology.read()
    model = model_from_json(topology)
    model.load_weights(weights)

    return model


def bright_predict(number):
    if number <= 0.3 or number >= 0.8:
        return 1
    else:
        return 0


def bright_vector(data):
    temp = []
    for string in data:
        temp.append(preproc.read_img(string, (500, 500, 3), color_mode='rgb'))
    score = []
    for item in temp:
        score.append(bright_predict(models.bright_model(item)))

    return score


def voting_predict():

    dist = glob.glob('/home/nick/Desktop/predict/noise/*')
    dist += glob.glob('/home/nick/Desktop/predict/light/*')
    dist += glob.glob('/home/nick/Desktop/predict/blur/*')

    undist = glob.glob('/home/nick/Desktop/predict/undist/*')

    blur_model = load_model('model/json/arch/blur.json',
                            'model/weights/blur.h5')
    noise_model = load_model(
        'model/json/arch/noise.json', 'model/weights/noise.h5')

    # data = glob.glob('/home/nick/Desktop/predict/blur/*')

    # blurred = preproc.load_imgs(data, (500, 500, 1), 'grayscale')

    score1 = blur_model.predict_classes(
        preproc.load_imgs(dist, (250, 250, 1), 'grayscale'))
    score2 = noise_model.predict_classes(
        preproc.load_imgs(dist, (500, 500, 1), 'grayscale'))
    score3 = bright_vector(dist)

    

   

    # X = np.concatenate((np.array(score1), np.array(score2),np.array(score3)), axis=1)
    # print(X.shape[0])


    predict = [np.array(score1),np.array(score2),np.array(score3)]
    predict = np.array(predict)
    y = np.ones(predict.shape[1])

    print(predict)
    print(y)


    score1 = blur_model.predict_classes(
        preproc.load_imgs(undist, (250, 250, 1), 'grayscale'))
    score2 = noise_model.predict_classes(
        preproc.load_imgs(undist, (500, 500, 1), 'grayscale'))
    score3 = bright_vector(undist)

    predictTemp =  [np.array(score1),np.array(score2),np.array(score3)]
    predictTemp = np.array(predictTemp)
    yTemp = np.zeros(predictTemp.shape[1])

    print(predictTemp)
    print(yTemp)  

    print(np.concatenate((predict,predictTemp)),axis=None)
    print(np.concatenate((y,yTemp)),axis=None)
    # Xtemp  = np.stack((np.array(score1), np.array(score2),np.array(score3)), axis=-1)
    # X = np.concatenate((X,Xtemp),axis=None)
    # y = np.concatenate((y, np.zeros(len(score3))), axis=None)

    # print(X)
    # print(y)

    # clf = svm.SVC(gamma='scale')

    # score1 = blur_model.predict_classes(preproc.load_imgs(data, (250, 250, 1), 'grayscale'))
    # score2 = noise_model.predict_classes(blurred)
    # print(score1)
    # print(score2)
    # temp = []
    # for string in data:
    #     temp.append(preproc.read_img(string, (500, 500, 3), color_mode='rgb'))

    # score3 = []
    # for item in temp:
    #     score3.append(models.bright_model(item))

    # print(score3)


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
