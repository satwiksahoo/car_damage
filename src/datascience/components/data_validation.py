import os
from src.datascience.logger import logger
from src.datascience.entity.config_entity import datavalidationconfig
import pandas as pd 


class dataValidation :
    def __init__(self , config : datavalidationconfig):
        self.config = config


    def validate_all_columns(self) -> bool:
     try:
            data = pd.read_csv(self.config.unzip_data_dir) 
            all_cols = list(data.columns)

            validation_status = True
            expected_columns = self.config.all_schema.keys()

            for col in expected_columns:
                if col not in all_cols:
                    validation_status = False
                    logger.warning(f'missing column: {col} ')
                    # with open(self.config.STATUS_FILE , 'w') as f:
                    #     f.write(f'validation status : {validation_status}')


                logger.info(f'validation status {validation_status}')
                # with open(self.config.STATUS_FILE , 'w') as f:
                #         f.write(f'validation status : {validation_status}')
                return validation_status     

     except Exception as e:
         logger.error(e)
         raise e 
           
    

    def save_validation_status(self , status : bool):

        with open(self.config.STATUS_FILE , 'w') as f:
            f.write(f'validation status : {status}')

        logger.info(f'validation status saved to {self.config.STATUS_FILE}')    


