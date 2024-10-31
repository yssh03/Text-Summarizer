from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.mode_evaluation import ModelEvaluation
from textSummarizer.entity import ModelEvaluationConfig


class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self) -> None:
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate()
