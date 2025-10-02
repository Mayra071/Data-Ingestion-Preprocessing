📌 Overview

This repository provides utilities for data ingestion, preprocessing, and schema validation.
It supports multiple data sources (CSV, JSON, SQL) and standard preprocessing steps, with data versioning handled by DVC.

🎯 Goals

Build connectors for:

CSV files

JSON files

SQL databases (local samples)

Implement preprocessing:

Missing value imputation

Feature scaling

Encoding categorical features

Validate schemas with Pandera

Store raw and pre-processed datasets with DVC

🛠️ Tech Stack

Python 3.9+

pandas for data manipulation

scikit-learn for preprocessing

pandera for schema validation

SQLAlchemy / sqlite3 for database connectors

DVC for dataset version control

📂 Repository Structure
.
├── artifacts/                # Raw & processed datasets (gitignored, tracked via DVC)
├── src/                      # Source code
│   ├── ingestion/            # Data ingestion connectors (CSV, JSON, SQL)
│   ├── preprocessing/        # Preprocessing utilities
│   ├── validation/           # Schema validation with Pandera
│   └── __init__.py
├── tests/                    # Unit tests
├── dvc.yaml                  # DVC pipeline definitions
├── requirements.txt          # Dependencies
├── README.md                 # Project documentation
└── .gitignore

📅 Day-wise Plan

Day 1: Define input sources (CSV, SQL). Implement Titanic CSV loader as baseline.

Day 2: Add preprocessing (missing values, scaling, encoding).

Day 3: Integrate schema validation with Pandera.

Day 4: Store raw + processed datasets using DVC.

Day 5: Demo ingestion pipeline + validation report.

🚀 Getting Started
1. Clone the repository
git clone https://github.com/<your-username>/data-ingestion-preprocessing.git
cd data-ingestion-preprocessing

2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run pipeline
dvc repro

✅ Example Usage
from src.ingestion.csv_loader import load_csv
from src.preprocessing.pipeline import preprocess_data
from src.validation.schema import validate_df

# Load dataset
df = load_csv("artifacts/train_data.csv")

# Preprocess
processed_df = preprocess_data(df)

# Validate
validate_df(processed_df)

📊 Deliverables

Data ingestion + preprocessing module

Schema validation with Pandera

Preprocessed datasets versioned with DVC

Validation report + demo pipeline