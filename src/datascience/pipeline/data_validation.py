from src.datascience.config.configuration import configurationManager
from src.datascience.components.data_validation import dataValidation
from src.datascience.logger import logger


STAGE_NAME  = 'DATA VALIDATION STAGE'

class data_validation_pipeline:
 
 def __init__(self):
    pass
 


 def initiate_data_validation(self):
    try:

        logger.info(f'>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<')

        config = configurationManager()
        data_validation_config = config.get_data_validation_config()

        data_validation = dataValidation(config = data_validation_config)

        validation_status = data_validation.validate_all_columns()
        data_validation.save_validation_status(validation_status)
        logger.info(f'>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<')

    except Exception as e:
        logger.error(e)
        raise e  
