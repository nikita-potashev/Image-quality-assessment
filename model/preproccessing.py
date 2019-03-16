import glob
import numpy as np
from keras.utils import np_utils
from keras.preprocessing import image

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

input_shape = (500, 500, 1)


def read_img(path):
    """[summary]
    
    Arguments:
        path {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    input_img = image.load_img(
        path, target_size=input_shape, color_mode="grayscale")
    input_img = image.img_to_array(input_img)
    return input_img


def load_img(lst):
    """[summary]
    
    Arguments:
        lst {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    arr = []
    for img_path in lst:
        arr.append(read_img(img_path))
    temp = np.array(arr, np.float32)
    return temp/255.0


raw_blur = glob.glob('models/Blur/data/train/blurry*.jpg')
raw_clear = glob.glob('models/Blur/data/train/clear*.jpg')

labels_blur = np.ones(len(raw_blur)).astype('int')
labels_clear = np.zeros(len(raw_clear)).astype('int')

raw_data = raw_blur + raw_clear
labels = np.concatenate((labels_blur, labels_clear), axis=0)

Y = np_utils.to_categorical(labels, 2)

x, y = shuffle(raw_data, Y, random_state=2)

X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.25, random_state=2)

X_train = load_img(X_train)
X_test = load_img(X_test)
