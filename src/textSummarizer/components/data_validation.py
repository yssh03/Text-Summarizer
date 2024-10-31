import os
from textSummarizer.entity import DataValidationConfig
from textSummarizer.logging import logger


class DataValidation:
    def __init__(self, config=DataValidationConfig):
        self.config = config

    def validate_data(self) -> bool:
        try:
            status = None
            files = os.listdir(os.path.join(
                "artifacts", "data_ingestion", "samsum"))
            for file in files:
                if file not in self.config.ALL_REQUIRED_FILE:
                    status = False
                    logger.info(f"Validation Status for {file}: {status}")
                else:
                    status = True
                    logger.info(f"Validation Status for {file}: {status}")
            return status
        except Exception as e:
            logger.error(f"Error in validation: {str(e)}")
            raise e
