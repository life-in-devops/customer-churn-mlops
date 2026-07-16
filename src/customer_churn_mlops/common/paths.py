from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

CONFIG_DIR = PROJECT_ROOT / "config"

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

RAW_DATASET = RAW_DATA_DIR / "customer_churn.csv"

TRAIN_DATASET = PROCESSED_DATA_DIR / "train.csv"
TEST_DATASET = PROCESSED_DATA_DIR / "test.csv"

SCHEMA_FILE = PROJECT_ROOT / "src" / "customer_churn_mlops" / "schemas" / "dataset_schema.yaml"
