import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib
from src.datascience.entity.config_entity import modeltrainerconfig
from src.datascience.logger import logger


class Modeltrainer:

    def __init__(self , config:modeltrainerconfig):
         self.config = config


    def train_and_save_model(self):
         
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


         rf_model = RandomForestRegressor()
         rf_model.fit(x_train_data , y_train_data)


         joblib.dump(rf_model , self.config.model_path)

         model_columns = x_train_data.columns.tolist()
         joblib.dump(model_columns, self.config.model_columns)


         prediction = rf_model.predict(x_test_data)

         logger.info(rf_model.score(x_test_data, y_test_data))
         logger.info(r2_score(y_test_data , prediction))
         logger.info(mean_absolute_error(y_test_data , prediction))
         logger.info(mean_squared_error(y_test_data , prediction))

              

