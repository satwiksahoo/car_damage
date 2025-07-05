import pandas as pd
from src.datascience.entity.config_entity import datatransformationconfig
from sklearn.model_selection import train_test_split
from src.datascience.logger import logger

class dataTransformation:
    def __init__(self , config : datatransformationconfig):

        self.config = config


    def data_cleaning(self , df:pd.DataFrame) -> pd.DataFrame:

        df['mileage'] = df['mileage'].str.extract(r'([\d.]+)').astype(float)

# 2. Clean and convert 'engine' (e.g., "1248 CC" → 1248.0)
        df['engine'] = df['engine'].str.extract(r'([\d.]+)').astype(float)

# 3. Clean and convert 'max_power' (e.g., "74 bhp" → 74.0)
        df['max_power'] = df['max_power'].str.extract(r'([\d.]+)').astype(float)

# 4. Optional: Extract numeric torque value (e.g., "190Nm@ 2000rpm" → 190.0)
        df['torque'] = df['torque'].str.extract(r'([\d.]+)').astype(float)



        df['mileage'] = df['mileage'].fillna(df['mileage'].median(), inplace=True)
        df['engine'] = df['engine'].fillna(df['engine'].median(), inplace=True)
        df['max_power'] =df['max_power'].fillna(df['max_power'].median(), inplace=True)
        df['torque'] = df['torque'].fillna(df['torque'].median(), inplace=True)
        df['seats'] = df['seats'].fillna(df['seats'].median(), inplace=True)

        return df
    

    def data_splitting(self , data_path : str) :

        df = pd.read_csv(data_path)


        transformed_df  =self.data_cleaning(df)
        
        train_set , test_set = train_test_split(transformed_df , test_size=0.3 , random_state=42)

        train_set.to_csv(self.config.transformed_train_path , index =False)
        test_set.to_csv(self.config.transformed_test_path , index =False)

        logger.info(f"Transformed train set saved to: {self.config.transformed_train_path}")
        logger.info(f"Transformed test set saved to: {self.config.transformed_test_path}")


        
