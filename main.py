from src.datascience.pipeline.data_ingestion import (data_ingestion_training_pipeline )
from src.datascience.pipeline.data_validation import data_validation_pipeline
from src.datascience.pipeline.data_transformation import data_transformation_pipeline
from src.datascience.pipeline.model_trainer import model_trainer_pipeline
from src.datascience.pipeline.model_evaluation import model_evaluation_pipeline
from src.datascience.logger import logger


STAGE_NAME = 'data ingestion stage' 

try :
    logger.info(f">>>>>>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<<<")

    ingestion = data_ingestion_training_pipeline()
    ingestion.initiate_data_ingestion()
    logger.info(f">>>>>>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<<<<")
    
except Exception as e:
    logger.exception(e)
    raise e   


STAGE_NAME = 'data validation stage'

try:
    logger.info(f'>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<')
    validation = data_validation_pipeline()
    validation.initiate_data_validation()
    logger.info(f'>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<')


except Exception as e:
    logger.error(e)
    raise e    


STAGE_NAME = 'data transformation stage'

try:
    logger.info(f'>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<')
    transformation = data_transformation_pipeline()
    transformation.initiate_data_transformation()
    logger.info(f'>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<')

except Exception as e:
    logger.error(e)
    raise e


STAGE_NAME = 'model training stage'

try:
    logger.info('>>>>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<')

    training = model_trainer_pipeline()
    training.initiate_model_training()

    logger.info('>>>>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<')

except Exception as e :
    logger.error(e)
    raise e    



STAGE_NAME = 'MODEL EVALUATION STAGE'

try:
    logger.info('>>>>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<')

    evaluation = model_evaluation_pipeline()
    evaluation.initiate_model_evaluation()

    logger.info('>>>>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<')

except Exception as e:
    logger.error(e)
    raise e

    

    


