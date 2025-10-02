from src.logger import logger
from src.exception import CustomException
from dotenv import load_dotenv
import sys

import os
import pandas as pd
import numpy as np

from src.utils import read_data

from dataclasses import dataclass

# data ingestion config
@dataclass
class DataIngestionConfig:
    db_data_path: str = os.path.join('artifacts', 'db_data.csv')
    jason_data_path: str = os.path.join('artifacts', 'jason_data.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logger.info("Entered the data ingestion method or component")
        try:
            df_db,df=read_data()
            logger.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logger.info(f'Head of df:\n {df.head(3)}')
            # database data path
            os.makedirs(os.path.dirname(self.ingestion_config.db_data_path), exist_ok=True)
            df_db.to_csv(self.ingestion_config.db_data_path, index=False, header=True)
            logger.info(f'Head of db:\n {df_db.head(3)}')
            
            logger.info("Ingestion of the data is completed")
            return (
                self.ingestion_config.raw_data_path,
                self.ingestion_config.db_data_path
            )
        
        
        except Exception as e:
            logger.info("Data ingestion fail")
            raise CustomException(e,sys)