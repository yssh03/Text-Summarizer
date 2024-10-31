from textSummarizer.logging import logger
from textSummarizer.entity import DataTransformationConfig
from transformers import AutoTokenizer
from datasets import load_from_disk
import os


class DataTransformation:
    def __init__(self, config=DataTransformationConfig) -> None:
        self.config = config

    def data_tokenizer(self, data) -> dict:
        try:
            tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer)
            input_embedding = tokenizer(
                data["dialogue"], max_length=1024, truncation=True)
            with tokenizer.as_target_tokenizer():
                target_encodings = tokenizer(
                    data["summary"], max_length=1024, truncation=True)

            return {
                'input_ids': input_embedding['input_ids'],
                'attention_mask': input_embedding['attention_mask'],
                'labels': target_encodings['input_ids']
            }
        except Exception as e:
            logger.info(f"Error in data_tokenizer: {str(e)}")
            raise e

    def get_data(self) -> None:
        try:
            samsum_data = load_from_disk(self.config.local_data)
            samsum_data_tokenized = samsum_data.map(
                self.data_tokenizer, batched=True)
            samsum_data_tokenized.save_to_disk(
                os.path.join(self.config.root_dir, "samsum"))

        except Exception as e:
            logger.info(f"Error in get_data: {str(e)}")
            raise e
