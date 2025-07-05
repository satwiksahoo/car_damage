from dataclasses import dataclass
from pathlib import Path

@dataclass

class dataIngestionconfig:
    root_dir : Path
    source_url : str
    local_data_file : Path
    unzip_dir : Path


@dataclass

class datavalidationconfig:
    root_dir : Path
    unzip_data_dir : Path
    STATUS_FILE : str
    all_schema : dict

@dataclass

class datatransformationconfig:
    root_dir : Path
    transformed_train_path : Path
    transformed_test_path : Path
    data_path : str


@dataclass

class modeltrainerconfig:
     root_dir : Path
     train_data_path : Path
     test_data_path : Path
     model_path : Path
     target_column : str
     model_columns : Path

@dataclass

class modelevaluationconfig:
    test_data_path : Path
    train_data_path : Path
    model_path : Path
    target_column : str
    mlflow_uri : str
