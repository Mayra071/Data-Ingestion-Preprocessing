📌 Overview

This repository implements a complete machine learning pipeline for predicting Titanic passenger survival using the famous Titanic dataset. The pipeline includes data ingestion from multiple sources (CSV and SQL database), schema validation, data preprocessing, model training, and evaluation. It leverages modern MLOps tools for experiment tracking, data versioning, and configuration management.

🎯 Goals

- Build a robust ML pipeline for Titanic survival prediction
- Implement data ingestion from CSV and SQL sources
- Perform schema validation using Pandera
- Apply preprocessing techniques: missing value imputation, feature scaling, categorical encoding
- Train and evaluate machine learning models
- Track experiments with MLflow
- Version datasets and models with DVC
- Use Hydra for configuration management

🛠️ Tech Stack

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Great Expectations](https://img.shields.io/badge/Great%20Expectations-0.17+-orange.svg)](https://greatexpectations.io/)
[![Evidently AI](https://img.shields.io/badge/Evidently%20AI-0.2+-purple.svg)](https://www.evidentlyai.com/)

- Python 3.9+
- pandas for data manipulation
- scikit-learn for preprocessing and modeling
- pandera for schema validation
- pymysql for SQL database connection
- hydra-core for configuration management
- MLflow for experiment tracking
- DVC for data and model versioning
- joblib for serialization
- matplotlib/seaborn for visualization

📂 Repository Structure
.
├── artifacts/                # Raw & processed datasets, models (gitignored, tracked via DVC)
│   ├── data.csv.dvc          # DVC tracked raw data
│   ├── db_data.csv.dvc       # DVC tracked database data
│   ├── train_data.csv.dvc    # Processed training data
│   ├── test_data.csv.dvc     # Processed test data
│   └── preprocessor.pkl.dvc  # Preprocessing pipeline
├── configs/                  # Hydra configuration files
│   └── config.yaml           # Main configuration
├── logs/                     # Application logs
├── mlartifacts/              # MLflow artifacts
├── mlruns/                   # MLflow experiment runs
├── notebook/                 # Jupyter notebooks for exploration
│   ├── Black_Box_explation.ipynb
│   └── img/
├── outputs/                  # Output files and reports
├── src/                      # Source code
│   ├── exception.py          # Custom exception handling
│   ├── logger.py             # Logging configuration
│   ├── schema_val.py         # Schema validation with Pandera
│   ├── utils.py              # Utility functions for data reading
│   └── Titanic/              # Titanic-specific modules
│       ├── components/       # Core components
│       │   ├── data_ingestion.py    # Data ingestion logic
│       │   ├── data_transfer.py     # Data transfer utilities
│       │   └── model_trainer.py     # Model training component
│       └── pipeline/         # Pipeline stages
│           ├── data_preprocessing.py  # Data preprocessing pipeline
│           ├── model_training.py      # Model training pipeline
│           └── model_evaluation.py    # Model evaluation pipeline
├── main.py                   # Main entry point with Hydra
├── requirements.txt          # Python dependencies
├── .dvcignore                # DVC ignore patterns
├── .gitignore                # Git ignore patterns
└── README.md                 # Project documentation

🚀 Getting Started

1. Clone the repository
   ```bash
   git clone <repository-url>
   cd titanic-ml-pipeline
   ```

2. Set up environment variables for database connection
   Create a `.env` file in the root directory:
   ```
   HOST=your_db_host
   USER=your_db_user
   PASSWORD=your_db_password
   DATABASE=your_db_name
   ```

3. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

5. Set up DVC
   ```bash
   dvc init
   dvc pull  # If DVC files are tracked
   ```

6. Run the ML pipeline
   ```bash
   python main.py
   ```

7. View MLflow experiments
   ```bash
   mlflow ui
   ```
   Open http://localhost:5000 in your browser


📊 Features

- **Multi-source Data Ingestion**: Supports CSV files and SQL databases
- **Schema Validation**: Ensures data quality with Pandera schemas
- **Automated Preprocessing**: Handles missing values, scaling, and encoding
- **Experiment Tracking**: Logs parameters, metrics, and models with MLflow
- **Data Versioning**: Tracks datasets and models with DVC
- **Configurable Pipeline**: Uses Hydra for flexible configuration
- **Comprehensive Logging**: Detailed logs for debugging and monitoring

📈 Pipeline Stages

1. **Data Ingestion**: Load data from CSV and SQL sources
2. **Schema Validation**: Validate data against predefined schemas
3. **Data Preprocessing**: Clean, transform, and split data
4. **Model Training**: Train ML models (to be implemented)
5. **Model Evaluation**: Evaluate model performance (to be implemented)

🔧 Configuration

The pipeline is configured via `configs/config.yaml`. Key settings include:
- Data paths and target column
- Model hyperparameters (test size, random state)
- Feature specifications (numerical and categorical)
- Visualization settings

📝 Notes

- Model training and evaluation components are currently placeholders and need implementation
- Ensure database credentials are set in `.env` file
- DVC is used for versioning artifacts; run `dvc add` to track new files
- Logs are saved in the `logs/` directory

---

## Author

Manish Kumar  
Email: aryam7842@gmail.com

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

MIT License

Copyright (c) 2024 Manish Kumar

