from CatsVsDogs.config import ConfigurationManager
from CatsVsDogs.components import Training , PrepareCallback
import tensorflow as tf


class TrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        tf.config.run_functions_eagerly(True)
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )