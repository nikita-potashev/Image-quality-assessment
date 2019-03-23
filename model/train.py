import argparse
import models
import preproc
import glob
import os

from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras import backend as k
import tensorflow as tf
import time


def train(dist,undist,args):
    X_train, X_test, y_train, y_test = preproc.load_data(
        dist, undist, args.input_shape, 0.25)
    model = models.blur_model(tuple(args.input_shape))

    current_time = time.strftime("%H:%M:%S", time.localtime())

    callbacks = [EarlyStopping(monitor='val_loss', patience=2),
                 ModelCheckpoint(filepath='weights/{}_{}.h5'.format(args.model,current_time),
                                 monitor='val_loss',
                                 save_best_only=True,
                                 mode='auto')
                 ]

    model.fit(X_train, y_train,
              callbacks=callbacks,
              batch_size=args.batch_size,
              epochs=args.num_epochs,
              verbose=2,
              validation_data=(X_test, y_test))
    score = model.evaluate(X_test, y_test, verbose=2)
    print('Test Loss:', score[0])
    print('Test accuracy:', score[1])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    config = tf.ConfigProto(intra_op_parallelism_threads=20, inter_op_parallelism_threads=20, \
                    allow_soft_placement=True, device_count = {'CPU': 1})
    session = tf.Session(config=config)
    k.set_session(session)

    parser.add_argument('--model', type=str)  # required = True
    parser.add_argument('--batch_size', type=int,
                        help='Batch size for model', default=32)
    parser.add_argument('--num_epochs', type=int,
                        help='Number of epochs', default=10)
    parser.add_argument('--train_mode', type=str,
                        help='cluster or pc(small dataset)', default='pc')
    parser.add_argument('--input_shape', nargs='+', type=int,
                        help='Height, width, channel size')

    args = parser.parse_args()
    print(os.getcwd())
    if args.model == "Blur":

        dist = glob.glob(
            'data/blur/train/All_Image_and_Kernels/blur*.jpg')

        dist += glob.glob(
            'data/blur/train/CERTH_ImageBlurDataset/TrainingSet/Artificially-Blurred/*')
        dist += glob.glob(
            'data/blur/train/CERTH_ImageBlurDataset/TrainingSet/Naturally-Blurred/*')
        dist += glob.glob(
            'data/blur/train/CERTH_ImageBlurDataset/EvaluationSet/DigitalBlurSet/Disk*')
        dist += glob.glob(
            'data/blur/train/CERTH_ImageBlurDataset/EvaluationSet/DigitalBlurSet/Gauss*')
        dist += glob.glob(
            'data/blur/train/CERTH_ImageBlurDataset/EvaluationSet/DigitalBlurSet/Motion*')

        undist = glob.glob('data/blur/train/image/*')
        undist += glob.glob('data/blur/train/All_Image_and_Kernels/im*.jpg')
        undist += glob.glob(
            'data/blur/train/CERTH_ImageBlurDataset/TrainingSet/Undistorted/*')
        undist += glob.glob(
            'data/blur/train/CERTH_ImageBlurDataset/EvaluationSet/DigitalBlurSet/Orig*')

        print(len(dist+undist))

        if args.train_mode == 'pc':
            dist = dist[:50]
            undist = undist[:50]
            train(dist,undist,args)
        if args.train_mode == 'cluster':
            train(dist,undist,args)

    if args.model == "Noise":
        print("Noise")
