from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_name: str
    local_data: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILE: list


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    local_data: Path
    tokenizer: str


@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    local_data: Path
    model: str


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data: Path
    model: Path
    tokenizer: Path
    metrics_file: Path


@dataclass(frozen=True)
class TrainingArgumentsConfig:
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    per_device_eval_batch_size: int
    weight_decay: int
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: int
    gradient_accumulation_steps: int
