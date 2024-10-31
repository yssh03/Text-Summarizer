from transformers import Trainer, TrainingArguments
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch
import os
from textSummarizer.entity import ModelTrainingConfig, TrainingArgumentsConfig
from datasets import load_from_disk


class ModelTrainer:
    def __init__(self, config=ModelTrainingConfig, config_trainer=TrainingArgumentsConfig) -> None:
        self.config = config
        self.config_trainer = config_trainer

    def model_training(self) -> None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model)
        model = AutoModelForSeq2SeqLM.from_pretrained(
            self.config.model).to(device)
        data_collator = DataCollatorForSeq2Seq(
            tokenizer=tokenizer, model=model)
        data = load_from_disk(self.config.local_data)
        training_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config_trainer.num_train_epochs,
            warmup_steps=self.config_trainer.warmup_steps,
            per_device_train_batch_size=self.config_trainer.per_device_train_batch_size,
            per_device_eval_batch_size=self.config_trainer.per_device_eval_batch_size,
            weight_decay=self.config_trainer.weight_decay,
            logging_steps=self.config_trainer.logging_steps,
            evaluation_strategy=self.config_trainer.evaluation_strategy,
            eval_steps=self.config_trainer.eval_steps,
            save_steps=self.config_trainer.save_steps,
            gradient_accumulation_steps=self.config_trainer.gradient_accumulation_steps
        )

        trainer = Trainer(
            model=model,
            args=training_args,
            tokenizer=tokenizer,
            train_dataset=data['train'],
            eval_dataset=data["validation"],
            data_collator=data_collator
        )

        trainer.train()

        model.save_pretrained(os.path.join(
            self.config.root_dir, "pegasus_model"))
        tokenizer.save_pretrained(os.path.join(
            self.config.root_dir, "tokenizer"))
