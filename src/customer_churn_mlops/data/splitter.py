from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from customer_churn_mlops.common.constants import (
    DEFAULT_RANDOM_STATE,
    TEST_SIZE,
)
from customer_churn_mlops.common.exceptions import DataValidationError
from customer_churn_mlops.common.logger import logger
from customer_churn_mlops.common.paths import (
    TEST_DATASET,
    TRAIN_DATASET,
)


class DataSplitter:
    """
    Split dataset into train and test datasets.
    """

    def split(
        self,
        df: pd.DataFrame,
    ) -> tuple[pd.DataFrame, pd.DataFrame]:
        """
        Split dataframe.

        Returns:
            train dataframe,
            test dataframe
        """

        logger.info("Starting train/test split.")

        if df.empty:
            raise DataValidationError("Cannot split empty dataset.")

        try:
            train_df, test_df = train_test_split(
                df,
                test_size=TEST_SIZE,
                random_state=DEFAULT_RANDOM_STATE,
                stratify=df["Churn"],
            )

            logger.info(f"Train shape: {train_df.shape}")

            logger.info(f"Test shape: {test_df.shape}")

            return train_df, test_df

        except Exception as exc:
            logger.exception("Train/test split failed.")

            raise DataValidationError(str(exc)) from exc

    def save(
        self,
        train_df: pd.DataFrame,
        test_df: pd.DataFrame,
    ) -> None:
        """
        Save processed datasets.
        """

        logger.info("Saving processed datasets.")

        Path(TRAIN_DATASET).parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        train_df.to_csv(
            TRAIN_DATASET,
            index=False,
        )

        test_df.to_csv(
            TEST_DATASET,
            index=False,
        )

        logger.info("Processed datasets saved successfully.")
