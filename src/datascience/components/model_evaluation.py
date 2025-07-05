from src.datascience.config.configuration import configurationManager
from src.datascience.entity.config_entity import modelevaluationconfig
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from src.datascience.logger import logger
import os
import joblib
import mlflow
import numpy as np
from urllib.parse import urlparse
import tempfile

os.environ['MLFLOW_TRACKING_URI'] = 'https://dagshub.com/satwiksahoojob/car_damage.mlflow'
os.environ['MLFLOW_TRACKING_USERNAME'] = 'satwiksahoojob'

os.environ['MLFLOW_TRACKING_PASSWORD'] =  '46df081cd1c771ae5c58838602b17d7d7c7de746'

mlflow.set_tracking_uri(os.environ['MLFLOW_TRACKING_URI'])


class modelevaluation:

    def __init__(self , config: modelevaluationconfig):
       self.config = config

    def initiate_model_evaluation(self):
     try:
 

        model  = joblib.load(self.config.model_path)

             
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

        mae = mean_absolute_error(y_test_data , prediction)
        mse = mean_squared_error(y_test_data , prediction)
        r2  = r2_score(y_test_data , prediction)
        rmse = np.sqrt(mse)

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme


        with mlflow.start_run():
           
           mlflow.log_metric("mae", mae)
           mlflow.log_metric("r2", r2)
           mlflow.log_metric("mse", mse)
           mlflow.log_metric("rmse", rmse)

           if tracking_uri_type_store != 'file':
              with tempfile.TemporaryDirectory() as tmp_dir:
                model_path = os.path.join(tmp_dir, "model.joblib")
                joblib.dump(model, model_path)
                
                mlflow.log_artifact(model_path, artifact_path="model")
           else:    
            print("Run logged in MLflow.")    

     except Exception as e:
        logger.error(e)
        raise e    



