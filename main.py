from textSummarizer.pipeline import data_ingestion, data_validation, data_transformation, model_trainer, model_evaluation
from textSummarizer.logging import logger


async def data_ingestion_stage():
    STAGE_NAME = "Data Ingestion stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_ingestion_main = data_ingestion.DataIngestionPipeline()
        data_ingestion_main.main()
        logger.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e


async def data_validation_stage():
    STAGE_NAME = "Data validation stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_validation_main = data_validation.DataValidationPipeline()
        data_validation_main.main()
        logger.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e


async def data_transformation_stage():
    STAGE_NAME = "Data transformation stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_transformation_main = data_transformation.DataTransformationPipeline()
        data_transformation_main.main()
        logger.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e


async def model_trainer_stage():
    STAGE_NAME = "Model Trainer stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_trainer_main = model_trainer.ModelTrainerPipeline()
        model_trainer_main.main()
        logger.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e


async def model_evaluation_stage():
    STAGE_NAME = "Model Evaluation stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_evaluation_main = model_evaluation.ModelEvaluationPipeline()
        model_evaluation_main.main()
        logger.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
