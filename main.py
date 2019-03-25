from keras.models import model_from_json
import glob
from model import preproc
import numpy as np 

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

    data = glob.glob('model/data/blur/train/image/*')
    print(len(data))
    s= 0
    for i in range(1000):
        img = preproc.read_img(data[i],(500,500,3),'rgb')
        r, g, b    = img[:, :, 0], img[:, :, 1], img[:, :, 2] 
        Y = (0.299*r+0.587*g+0.114*b)
     
        Ymax = np.max(Y)
        Y= np.sum(Y)/(500*500)
        s+=Y/Ymax
    print(s/1000)
        