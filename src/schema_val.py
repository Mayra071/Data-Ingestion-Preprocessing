import pandas as pd
import pandera.pandas as pa
from pandera.pandas import DataFrameSchema, Column, Check
from pandera import Column, DataFrameSchema, Check
from src.utils import read_data
import sys
from src.exception import CustomException
from src.logger import logger

def schema():
    try:
        # Define schema
        
        logger.info("Schema Validation staeted!")
        titanic_schema = DataFrameSchema({
            "PassengerId": Column(int, Check.greater_than(0)),
            "Survived": Column(int, Check.isin([0, 1])),
            "Pclass": Column(int, Check.isin([1, 2, 3])),
            "Name": Column(str, nullable=False),
            "Sex": Column(str, Check.isin(["male", "female"])),
            "Age": Column(float, Check.in_range(0, 100), nullable=True),
            "SibSp": Column(int, Check.greater_than_or_equal_to(0)),
            "Parch": Column(int, Check.greater_than_or_equal_to(0)),
            "Ticket": Column(str, nullable=False),
            "Fare": Column(float, Check.greater_than_or_equal_to(0)),
            "Cabin": Column(str, nullable=True),
            "Embarked": Column(str, Check.isin(["C", "Q", "S"]), nullable=True)
        })

        # Example: load Titanic data (CSV)
        _, df = read_data()

        # Validate DataFrame
        validated_df = titanic_schema.validate(df)
        logger.info("Schema validation completed successfully")
        
    except Exception as e:
        logger.info('Validation Not successful.')
        raise CustomException(e,sys)
