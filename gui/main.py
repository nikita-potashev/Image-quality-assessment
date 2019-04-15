from models.blur_model import BlurModel
from tensorflow.python.keras.models import load_model
import tensorflow as tf

def app(config):
    blur = BlurModel.build_model1(config)
    print(blur.summary())
    # blur.load_weights('experiments/blur_model1/checkpoint/blur_model1-07-0.07.h5')
    # blur.predict_classes('')
    # blur = tf.contrib.saved_model.load_keras_model('experiments/blur_model1/checkpoint')

