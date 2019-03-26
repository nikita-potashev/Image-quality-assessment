from keras.layers import (Activation, Conv2D, Dense, Dropout, Flatten,
                          MaxPooling2D)
from keras.models import Sequential


def blur_model(input_shape):
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

    model.add(Dense(2, activation='sigmoid'))

    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    return model


def noise_model(input_shape):
    """[summary]

    Arguments:
        input_shape [tuple] -- Height,Width,Channels of image

    Returns:
        [model] -- simple cnn model
    """

    model = Sequential()
    model.add(Conv2D(32, 5, 5, input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    model.add(Conv2D(64, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))

    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    model.add(Dense(2))
    model.add(Activation('sigmoid'))

    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    return model


def bright_model(img, input_shape):
    """[summary]

    Arguments:
        input_shape {[type]} -- [height,hidth,channels of image]
        img {[n]}
    Returns:
        [float] -- [ [0,1] bright coef of image ]
    """
    r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    Y = (0.299*r+0.587*g+0.114*b)  # coefs rec by FCC
    Ymax = np.max(Y)
    Y = np.sum(Y)/(input_shape[0]*input_shape[1])

    return Y/Ymax
