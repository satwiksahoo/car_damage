import os
import urllib.request as request
import zipfile
# from src.datascience import logger
from src.datascience.logger import logger

from src.datascience.entity.config_entity import dataIngestionconfig
from src.datascience.utils.common import get_size, create_directories
from pathlib import Path


class dataIngestion:

    def __init__(self , config : dataIngestionconfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading data from {self.config.source_url} to {self.config.local_data_file}")

            filename, headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )


            logger.info(f"Download completed. File size: {get_size(Path(self.config.local_data_file))}")

        else:
            logger.info(f"File already exists at {self.config.local_data_file}, skipping download.")



    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        logger.info(f"Extracted zip file to {unzip_path}")                



