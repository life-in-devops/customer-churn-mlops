import pandas as pd

from customer_churn_mlops.common.logger import logger
from customer_churn_mlops.common.paths import RAW_DATASET
from customer_churn_mlops.data.loader import load_csv


class DataIngestion:
    """
    Handles data ingestion.
    """

    def ingest(self) -> pd.DataFrame:
        logger.info("Starting data ingestion.")

        df = load_csv(RAW_DATASET)

        logger.info("Data ingestion completed.")

        return df
