from src.datascience.pipeline.data_ingestion import (data_ingestion_training_pipeline )
from src.datascience.pipeline.data_validation import data_validation_pipeline
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


