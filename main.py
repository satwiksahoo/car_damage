from src.datascience.pipeline.data_ingestion import data_ingestion_training_pipeline
from src.datascience import logger


STAGE_NAME = 'data ingestion stage' 

try :
    logger.info(f">>>>>>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<<<<<")

    ingestion = data_ingestion_training_pipeline()
    ingestion.initiate_data_ingestion()
    logger.info(f">>>>>>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<<<<")
    
except Exception as e:
    logger.exception(e)
    raise e    


