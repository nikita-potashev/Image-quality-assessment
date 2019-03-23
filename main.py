from keras.models import model_from_json
import glob
from model import preproc

if __name__ == "__main__":
    json_file = open("model/json/blur.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()
    # Создаем модель на основе загруженных данных
    model = model_from_json(loaded_model_json)
    # Загружаем веса в модель
    model.load_weights("model/weights/blur.h5")

    data = glob.glob('/home/nick/Desktop/databrelease2/gblur/*.bmp')