class BaseEnsembleTrain:
    def __init__(self, models, data_train, data_test, config):
        self.models = models
        self.data_train = data_train
        self.data_test = data_test
        self.config = config

    def train(self):
        raise NotImplementedError
