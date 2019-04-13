from data_loader.data_loader import DataLoader
from models.blur_ensemble import BlurEnsemble
from trainers.blur_ensemble_trainer import BlurEnsembleTrainer
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
    # create_dirs([config.summary_dir, config.checkpoint_dir, config.visual_dir])

    print('Create the data generator.')
    data_generator = DataLoader(config)

    print('Create the model.')
    models = BlurEnsemble(config)

    print('Create the trainer')
    trainer = BlurEnsembleTrainer(models.models, data_generator.get_train_data(), data_generator.get_test_data(), config)

    print('Start training the model.')
    trainer.train_gen()

    print('Visualize the losses')
    # trainer.visualize()


if __name__ == '__main__':
    main()
