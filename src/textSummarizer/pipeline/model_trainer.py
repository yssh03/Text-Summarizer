from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_trainer import ModelTrainer


class ModelTrainerPipeline:
    def __init__(self) -> None:
        pass

    def main(self) -> None:
        config = ConfigurationManager()
        model_trainer_config, training_arguments_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(
            config=model_trainer_config, config_trainer=training_arguments_config)
        model_trainer.model_training()
