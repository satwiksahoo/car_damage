from src.datascience.config.configuration import configurationManager
from src.datascience.components.model_trainer import Modeltrainer
from src.datascience.logger import logger

STAGE_NAME = 'MODEL TRAINER PIPELINE'


class model_trainer_pipeline:


   def __init__(self):
      pass
   

   def initiate_model_training(self):
      
      try:
         logger.info(f'>>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<<<<<<')

         config = configurationManager()
         model_training_config = config.get_model_trainer_config()
         model_trainer = Modeltrainer(config = model_training_config)
         model_trainer.train_and_save_model()

         logger.info(f'>>>>>>>>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<<<<<<')

      except Exception as e :
         logger.error(e)
         raise e   

