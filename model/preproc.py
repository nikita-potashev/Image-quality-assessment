import glob
import numpy as np
from keras.utils import np_utils
from keras.preprocessing import image

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split


def read_img(path, input_shape, color_mode=''):
    """[summary]

    Arguments:
        path {[string]}
        input_shape {[tuple]} -- target shape

    Returns:
        [numpy array] -- return image as numpy array
    """
    input_img = image.load_img(
        path, target_size=input_shape, color_mode=color_mode)
    input_img = image.img_to_array(input_img)
    return input_img


def load_imgs(lst, input_shape, color_mode=''):
    """[summary]

    Arguments:
        lst {[list]} 

    Returns:
        [numpy array] -- return image as numpy array
    """
    arr = []
    for img_path in lst:
        arr.append(read_img(img_path, input_shape, color_mode))
    temp = np.array(arr, np.float32)
    return temp/255.0


def load_data(distorted_path, undistorted_path, input_shape, test_size, color_mode=''):
    """[summary]

    Arguments:
        distorted_path {[string]} -- [path to distored images folder]
        undistorted_path {[string]} -- [path to distored images folder]
        input_shape {[tuple]} -- [height,hidth,channels of image]
        test_size {[float]} -- [test size to split]

    Keyword Arguments:
        color_mode {string} -- [grayscale(to decrease memory using)] (default: {none})

    Returns:
        [tuple] -- [test,train data and labels]
    """
    # parse all files
    dist = glob.glob(distorted_path)
    undist = glob.glob(undistorted_path)
    # labels for images
    labels_dist = np.ones(len(dist)).astype('int')
    labels_undist = np.zeros(len(undist)).astype('int')

    data = dist + undist
    labels = np.concatenate((labels_dist, labels_undist), axis=0)
    # binary classification
    categories = np_utils.to_categorical(labels, 2)
    # data and labels
    x, y = shuffle(data, categories, random_state=2)

    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=test_size, random_state=2)

    return (X_train, X_test, y_train, y_test)
