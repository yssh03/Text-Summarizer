from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directory
from textSummarizer.entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainingConfig,
    TrainingArgumentsConfig,
    ModelEvaluationConfig
)


class ConfigurationManager:
    def __init__(self, config_file=CONFIG_FILE_PATH, params_file=PARAMS_FILE_PATH):
        self.config = read_yaml(config_file)
        create_directory([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directory([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_name=config.source_name,
            local_data=config.local_data
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directory([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILE=config.ALL_REQUIRED_FILE
        )

        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directory([config.root_dir])
        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            local_data=config.local_data,
            tokenizer=config.tokenizer
        )

        return data_transformation_config

    def get_model_trainer_config(self) -> tuple[ModelTrainingConfig, TrainingArgumentsConfig]:
        config = self.config.model_trainer
        config_training = self.config.training_arguments
        create_directory([config.root_dir])
        model_trainer_config = ModelTrainingConfig(
            root_dir=config.root_dir,
            local_data=config.local_data,
            model=config.model
        )

        training_argument_config = TrainingArgumentsConfig(
            num_train_epochs=config_training.num_train_epochs,
            warmup_steps=config_training.warmup_steps,
            per_device_eval_batch_size=config_training.per_device_eval_batch_size,
            per_device_train_batch_size=config_training.per_device_train_batch_size,
            weight_decay=config_training.weight_decay,
            logging_steps=config_training.logging_steps,
            evaluation_strategy=config_training.evaluation_strategy,
            eval_steps=config_training.eval_steps,
            save_steps=config_training.save_steps,
            gradient_accumulation_steps=config_training.gradient_accumulation_steps
        )

        return model_trainer_config, training_argument_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        create_directory([config.root_dir])
        
        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            model=config.model,
            data=config.data,
            metrics_file=config.metrics_file,
            tokenizer=config.tokenizer
        )

        return model_evaluation_config
