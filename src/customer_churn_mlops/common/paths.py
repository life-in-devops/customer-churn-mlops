from pathlib import Path

from customer_churn_mlops.common.constants import (
    FEATURE_NAMES_FILE,
    MODEL_NAME,
    PREPROCESSOR_NAME,
    TEST_DATASET,
    TRAIN_DATASET,
)

# Project Root
ROOT_DIR = Path(__file__).resolve().parents[3]

# Data Directories
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Dataset Paths
TRAIN_DATA_PATH = PROCESSED_DATA_DIR / TRAIN_DATASET
TEST_DATA_PATH = PROCESSED_DATA_DIR / TEST_DATASET

# Artifact Directory
ARTIFACTS_DIR = ROOT_DIR / "storage"
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

# Artifact Paths
PREPROCESSOR_PATH = ARTIFACTS_DIR / PREPROCESSOR_NAME
MODEL_PATH = ARTIFACTS_DIR / MODEL_NAME
FEATURE_NAMES_PATH = ARTIFACTS_DIR / FEATURE_NAMES_FILE
