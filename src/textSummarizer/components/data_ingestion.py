import os
from textSummarizer.entity import DataIngestionConfig
from datasets import load_dataset, load_from_disk
from textSummarizer.logging import logger
from typing import Any


class DataIngestion:
    def __init__(self, config=DataIngestionConfig):
        self.config = config

    def save_dataset(self) -> None:
        try:
            if not os.path.exists(self.config.local_data):
                dataset = load_dataset(
                    self.config.source_name, trust_remote_code=True)
                dataset.save_to_disk(self.config.local_data)
                logger.info("dataset has been saved successfully!")
            else:
                logger.info("Error while saving the dataset.")

        except Exception as e:
            raise e

    def load_dataset(self) -> Any:
        try:
            data = load_from_disk(self.config.local_data)
            return data
        except Exception as e:
            raise e
