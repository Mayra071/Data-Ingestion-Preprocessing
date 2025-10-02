import os
import sys
from src.exception import CustomException
from src.logger import logger
import pandas as pd
import numpy as np
import pymysql
from dotenv import load_dotenv
# Generic functionality for data reading


# read data from from my local system
load_dotenv()

host = os.getenv("HOST")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")



# function to read data
def read_data():
    
    """Reads data from database.

    """
    logger.info("Reading data from database")
    try:
        mydb=pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
        )
        
        # SQL database connector
        logger.info("Successfully connected to the database")
        df_db=pd.read_sql('select * from titanic_dataset', con=mydb)
        
        # csv connector
        file_path = r'C:\Company\Data_Set\Titanic-Dataset.csv'
        df = pd.read_csv(file_path)
        logger.info(f"Data read successfully from {file_path}")
        
        # json connector
        # file_path_j =r'C:\Company\Data_Set\Titanic-Dataset.json'
        # df_json = pd.read_json(file_path_j)
        # logger.info(f"json Data read successfully from {file_path_j}")
        
        return df_db, df
    except Exception as e:
        raise CustomException(e, sys)