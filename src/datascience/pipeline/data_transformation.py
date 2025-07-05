from src.datascience.config.configuration import configurationManager
from src.datascience.components.data_transformation import dataTransformation
from src.datascience.logger import logger


STAGE_NAME = 'data transformation stage'

class data_transformation_pipeline:
     
     def __init__(self):
          pass 
     def initiate_data_transformation(self):
          
        try:
               logger.info(f">>>>>> a>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<<<")

               config = configurationManager()
               data_transformation_config = config.get_data_transformation_config()
               data_transformation = dataTransformation(config = data_transformation_config)

               data_transformation.data_splitting(data_path = data_transformation_config.data_path)

               logger.info(f">>>>>> a>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<<<<")

        except Exception as e:    
             
             logger.error(e)
             raise e


