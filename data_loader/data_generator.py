import glob

import numpy as np
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.utils import np_utils
from sklearn.model_selection import train_test_split


class DataGenerator:
    def __init__(self, config):
        distorted_paths = config.distorted
        undistorted_paths = config.undistorted

        dist = []
        undist = []

        for path in distorted_paths:
            dist += glob.glob(path, recursive=True)
        for path in undistorted_paths:
            undist += glob.glob(path, recursive=True)

        print(config.debug)
        if config.debug:
            dist = dist[:10]
            undist = undist[:10]

        labels_dist = np.ones(len(dist)).astype('int')
        labels_undist = np.zeros(len(undist)).astype('int')

        data = dist + undist
        labels = np.concatenate((labels_dist, labels_undist), axis=0)
        # binary classification
        categories = np_utils.to_categorical(labels, 2)

        X_train, X_test, Y_train, Y_test = train_test_split(
            data, categories, test_size=config.validation_split, random_state=2)

        self.X_train = load_imgs(X_train, (500, 500, 1), config.color_mode)
        self.X_test = load_imgs(X_test, (500, 500, 1), config.color_mode)

        self.Y_train = Y_train
        self.Y_test = Y_test

    def get_train_data(self):
        return self.X_train, self.Y_train

    def get_test_data(self):
        return self.X_test, self.Y_test


def read_img(path, input_shape, color_mode='grayscale'):
    input_img = image.load_img(
        path, target_size=input_shape, color_mode=color_mode)
    input_img = image.img_to_array(input_img)
    return input_img


def load_imgs(lst, input_shape, color_mode=''):
    arr = []
    for img_path in lst:
        arr.append(read_img(img_path, input_shape, color_mode))
    temp = np.array(arr, np.float32)
    return temp/255.0
