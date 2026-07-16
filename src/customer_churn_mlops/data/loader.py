from pathlib import Path

import pandas as pd

from customer_churn_mlops.common.exceptions import DataValidationError
from customer_churn_mlops.common.logger import logger


def load_csv(path: Path) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.
    """

    logger.info(f"Loading dataset from: {path}")

    if not path.exists():
        raise DataValidationError(f"Dataset not found: {path}")

    try:
        df = pd.read_csv(path)

        logger.info(f"Dataset loaded successfully. Shape: {df.shape}")

        return df

    except Exception as exc:
        logger.exception("Failed to load dataset.")
        raise DataValidationError(str(exc)) from exc
