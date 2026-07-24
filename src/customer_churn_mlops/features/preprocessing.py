import pandas as pd

from customer_churn_mlops.common.constants import (
    ID_COLUMN,
    TARGET_COLUMN,
)


class DataPreprocessor:
    """Handles basic dataset cleaning."""

    @staticmethod
    def clean(df: pd.DataFrame) -> pd.DataFrame:
        """
        Perform basic data cleaning.

        Steps
        -----
        1. Remove customerID
        2. Convert TotalCharges to float
        3. Convert Churn to binary
        """

        df = df.copy()

        # Drop ID column
        if ID_COLUMN in df.columns:
            df = df.drop(columns=[ID_COLUMN])

        # Clean TotalCharges
        df["TotalCharges"] = df["TotalCharges"].replace(" ", pd.NA).astype(float)

        # Fill missing values with median
        df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

        # Encode target
        if TARGET_COLUMN in df.columns:
            df[TARGET_COLUMN] = df[TARGET_COLUMN].map({"Yes": 1, "No": 0}).astype(int)

        return df
