from src.datascience.config.configuration import configurationManager
from src.datascience.entity.config_entity import modelevaluationconfig
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from src.datascience.logger import logger

import joblib


class modelevaluation:

    def __init__(self , config: modelevaluationconfig):
       self.config = config

    def initiate_model_evaluation(self):
     try:

        

        model = joblib.load(self.config.model_path)

        # test_data  = pd.read_csv(self.config.test_data_path)
        # train_data = pd.read_csv(self.config.train_data_path)

        # x_test_data = test_data.drop([self.config.target_column] , axis = 1)
        # y_test_data = test_data[self.config.target_column]


        # x_train_data = train_data.drop([self.config.target_column] , axis = 1)
        # y_train_data = train_data[self.config.target_column]



        
        # x_test_data = pd.get_dummies(x_test_data, drop_first=True)  #



        # x_test_data = x_test_data.reindex(columns=x_train_data.columns, fill_value=0) #

             
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        x_train_data = train_data.drop([self.config.target_column] , axis = 1)
        y_train_data = train_data[self.config.target_column]



        x_test_data = train_data.drop([self.config.target_column] , axis = 1)
        y_test_data = train_data[self.config.target_column]


        x_train_data = pd.get_dummies(x_train_data, drop_first=True)  #
        x_test_data = pd.get_dummies(x_test_data, drop_first=True)  #

    # Align test to train columns
        x_test_data = x_test_data.reindex(columns=x_train_data.columns, fill_value=0) #

        



        prediction = model.predict(x_test_data)


        logger.info(model.score(x_test_data, y_test_data))
        logger.info(r2_score(y_test_data , prediction))
        logger.info(mean_absolute_error(y_test_data , prediction))
        logger.info(mean_squared_error(y_test_data , prediction))

     except Exception as e:
        logger.error(e)
        raise e    



