import numpy as np
from keras.layers import (Activation, Conv2D, Dense, Dropout, Flatten,
                          MaxPooling2D)
from keras.models import Sequential


def blur_model(input_shape,metric,last_activ,loss):
    """[summary]

    Arguments:
        input_shape [tuple] -- height,hidth,channels of image

    Returns:
        [model] -- simple cnn model
    """
    model = Sequential()
    model.add(Conv2D(8, (5, 5), activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    model.add(Conv2D(16, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))

    model.add(Flatten())
    model.add(Dense(32, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(16, activation='relu'))
    model.add(Dropout(0.3))

    model.add(Dense(2, activation=last_activ))

    model.compile(loss=loss
                  optimizer='adam',
                  metrics=[metric])
    return model


def noise_model(input_shape,metric,last_activ,loss):
    """[summary]

    Arguments:
        input_shape [tuple] -- Height,Width,Channels of image

    Returns:
        [model] -- simple cnn model
    """

    model = Sequential()
    model.add(Conv2D(4, 3, 3, input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    model.add(Conv2D(8, 5, 5))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))

    model.add(Flatten())
    model.add(Dense(16))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    model.add(Dense(2))
    model.add(Activation(last_activ))

    model.compile(loss=loss,
                  optimizer='adam',
                  metrics=[metric])
    return model


def bright_model(img):
    """[summary]

    Arguments:
        img {[numpy_array]} -- [image as np array]
    Returns:
        [float] -- [ [0,1] bright coef of image ]
    """
    r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    Y = (0.299*r+0.587*g+0.114*b)  # coefs rec by FCC
    Ymax = np.max(Y)
    Y = np.sum(Y)/(img.shape[0]*img.shape[1])

    return Y/Ymax
