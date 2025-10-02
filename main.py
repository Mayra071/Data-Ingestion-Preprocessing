import hydra
from omegaconf import DictConfig, OmegaConf
from src.logger import logger
from src.exception import CustomException
from dotenv import load_dotenv
import sys
from src.schema_val import schema
import os
import pandas as pd
import numpy as np

from src.Titanic.components.data_ingestion import DataIngestion,DataIngestionConfig
from src.Titanic.pipeline.data_preprocessing import DataPreprocessor

@hydra.main(config_path="configs", config_name="config", version_base=None)
def main(cfg: DictConfig):
    logger.info("Application started")
    # Your application code here
    try:
        
        # Data Ingestion
        data_ingestion = DataIngestion()
        row_data_path, db_data_path=data_ingestion.initiate_data_ingestion()
        logger.info("Data ingestion completed successfully")
        
        # Schema validation
        schema()

        # Data Preprocessing
        preprocessor = DataPreprocessor(cfg)
        train_data, test_data, feature_columns = preprocessor.split_data(row_data_path)

        logger.info("Data preprocessing completed successfully")
        

    except Exception as e:
        logger.info("An error occurred")
        raise CustomException(e, sys)

if __name__ == "__main__":
    main()
