from src.datascience.logger import logger
from src.datascience.components.model_evaluation import modelevaluation
from src.datascience.config.configuration import configurationManager


STAGE_NAME = 'MODEL EVALUATION PIPELINE'

class model_evaluation_pipeline:

    def initiate_model_evaluation(self):
     try:

        logger.info(f'>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<<<')

        config = configurationManager()
        model_evaluation_config = config.get_model_evaluation_config()

        model_evaluation_obj = modelevaluation(config = model_evaluation_config)
        model_evaluation_obj.initiate_model_evaluation()

        logger.info(f'>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<<')

     except Exception as e:
        logger.error(e)
        raise e    









