import os
from box.exceptions import BoxValueError
import yaml
from src.datascience.logger import logger
from ensure import ensure_annotations
from box import ConfigBox  # Makes config.yaml access easy (e.g., config.data_ingestion.source_url)
from pathlib import Path

@ensure_annotations
def read_yaml(path_to_yaml) -> ConfigBox:
    """Reads YAML file and returns ConfigBox (e.g., dict-like object with dot notation)"""
    try:
        with open(str(path_to_yaml)) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(paths: list, verbose=True):
    """Creates list of directories"""
    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")




@ensure_annotations
def get_size(path: Path) -> str:
    """Returns the size of a file in KB"""
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
