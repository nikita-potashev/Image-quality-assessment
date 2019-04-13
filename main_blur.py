from data_loader.data_loader import DataLoader
from models.blur_model import BlurModel
from trainers.blur_model_trainer import BlurModelTrainer
from utils.config import process_config
from utils.dirs import create_dirs
from utils.utils import get_args


def main():
    # capture the config path from the run arguments
    # then process the json configuration file
    try:
        args = get_args()
        config = process_config(args.config)
    except:
        print("missing or invalid arguments")
        exit(0)


    # create the experiments dirs
    create_dirs([config.summary_dir, config.checkpoint_dir, config.visual_dir])

    models = {

        'blur_model1' : BlurModel.build_model1(config),
        'blur_model2' : BlurModel.build_model2(config),
        'blur_model3' : BlurModel.build_model3(config)
    }

    print('Create the data generator.')
    data_generator = DataLoader(config)

    print('Create the model.')
    model = models[config.exp_name]

    print('Create the trainer')
    trainer = BlurModelTrainer(model, data_generator.get_train_data(), config)

    print('Start training the model.')
    trainer.train()

    print('Visualize the losses')
    trainer.visualize()


if __name__ == '__main__':
    main()
