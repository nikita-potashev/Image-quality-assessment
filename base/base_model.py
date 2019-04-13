class BaseModel:
    def __init__(self, config):
        self.config = config
        self.model = None

    def save(self, checkpoint_path):
        if self.model is None:
            raise Exception("You have to build the model first.")

        print("Saving model...")
        self.model.save_weights(checkpoint_path)
        print("Model saved")

    def load(self, checkpoint_path):
        if self.model is None:
            raise Exception("You have to build the model first.")

        print("Loading model checkpoint {} ...\n".format(checkpoint_path))
        self.model.load_weights(checkpoint_path)
        print("Model loaded")

    def build_model(self):
        raise NotImplementedError

    def predict(self, data, batch_size=None, verbose=0, steps=None, callbacks=None):
        self.model.predict(data, batch_size=batch_size, verbose=verbose, steps=steps, callbacks=callbacks)

    def predict_classes(self, data, batch_size=32, verbose=1):
        self.model.predict_classes(self, data, batch_size=batch_size, verbose=verbose)
