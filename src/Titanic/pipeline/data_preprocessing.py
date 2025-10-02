"""
Data preprocessing module for feature engineering and data cleaning.
"""
import sys
import os
from src.logger import logger
from src.exception import CustomException
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import joblib

class DataPreprocessor:
    """Class for data preprocessing and feature engineering."""

    def __init__(self, cfg):
        self.cfg = cfg
        self.numerical_features = list(self.cfg.model.features.numerical)
        self.categorical_features = list(self.cfg.model.features.categorical)
        self.target_column = self.cfg.model.target_column
        self.test_size = self.cfg.model.test_size
        self.random_state = self.cfg.model.random_state
        self.drop_columns = list(self.cfg.model.drop_columns)
        self.train_data_path = os.path.join('artifacts', 'train_data.csv')
        self.test_data_path = os.path.join('artifacts', 'test_data.csv')
        self.processed_obj_path = os.path.join("artifacts", "preprocessor.pkl")

        # Create preprocessing pipeline
        num_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])

        cat_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OneHotEncoder(handle_unknown='ignore', drop='first'))
        ])

        self.preprocessor = ColumnTransformer([
            ('num', num_pipeline, self.numerical_features),
            ('cat', cat_pipeline, self.categorical_features)
        ])

    def get_feature_names(self):
        """Get feature names after transformation."""
        try:
            num_features = self.numerical_features
            cat_encoder = self.preprocessor.named_transformers_['cat']['encoder']
            cat_features = cat_encoder.get_feature_names_out(self.categorical_features)
            return list(num_features) + list(cat_features)
        except:
            return self.numerical_features + self.categorical_features

    def split_data(self, path):
        """Preprocess the data and split into train/test sets."""
        try:
            # Drop unnecessary columns
            df=pd.read_csv(path)
            df = df.drop(columns=[c for c in self.drop_columns if c in df.columns])

            # Split into features and target
            X = df.drop(columns=[self.target_column])
            y = df[self.target_column]

            # Train-test split
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=self.test_size, random_state=self.random_state, stratify=y
            )

            # Fit preprocessor on training data
            X_train_processed = self.preprocessor.fit_transform(X_train)
            X_test_processed = self.preprocessor.transform(X_test)

            # Get feature names
            feature_names = self.get_feature_names()

            # Create DataFrames
            train_df = pd.DataFrame(X_train_processed, columns=feature_names)
            train_df[self.target_column] = y_train.values

            test_df = pd.DataFrame(X_test_processed, columns=feature_names)
            test_df[self.target_column] = y_test.values

            # Save train and test data
            os.makedirs(os.path.dirname(self.train_data_path), exist_ok=True)
            train_df.to_csv(self.train_data_path, index=False)
            logger.info(f'Training data:\n {train_df.head(4)}')

            os.makedirs(os.path.dirname(self.test_data_path), exist_ok=True)
            test_df.to_csv(self.test_data_path, index=False)
            logger.info(f'Test data :\n {test_df.head(4)}')

            # Save preprocessor
            joblib.dump(self.preprocessor, self.processed_obj_path)

            logger.info(f"Train data shape: {train_df.shape}")
            logger.info(f"Test data shape: {test_df.shape}")
            logger.info(f"Preprocessor saved at {self.processed_obj_path}")

            return self.train_data_path, self.test_data_path, feature_names

        except Exception as e:
            logger.error("Error in preprocessing and splitting data")
            raise CustomException(e, sys)
