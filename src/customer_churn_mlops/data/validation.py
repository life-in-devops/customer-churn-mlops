from pathlib import Path

import pandas as pd
import yaml

from customer_churn_mlops.common.exceptions import DataValidationError
from customer_churn_mlops.common.logger import logger
from customer_churn_mlops.common.paths import SCHEMA_FILE


class DataValidation:
    """
    Validate dataset against predefined schema and quality checks.
    """

    def __init__(self, schema_path: Path = SCHEMA_FILE):
        """
        Load dataset schema configuration.

        Args:
            schema_path: Path to YAML schema file.
        """

        try:
            self.schema = yaml.safe_load(schema_path.read_text(encoding="utf-8"))

        except Exception as exc:
            raise DataValidationError(f"Unable to load schema file: {schema_path}") from exc

    def validate(self, df: pd.DataFrame) -> bool:
        """
        Execute all validation checks.

        Args:
            df: Input dataframe.

        Returns:
            True if validation completes successfully.

        Raises:
            DataValidationError: If critical validation fails.
        """

        logger.info("Starting data validation.")

        self.validate_empty_dataset(df)

        self.validate_columns(df)

        self.validate_target_column(df)

        self.validate_missing_values(df)

        self.validate_duplicates(df)

        logger.info("Data validation completed successfully.")

        return True

    def validate_empty_dataset(self, df: pd.DataFrame) -> None:
        """
        Check whether dataframe contains data.
        """

        if df.empty:
            raise DataValidationError("Dataset is empty.")

    def validate_columns(self, df: pd.DataFrame) -> None:
        """
        Validate required columns exist.
        """

        logger.info("Checking required columns.")

        expected_columns = self.schema["columns"]

        missing_columns = [column for column in expected_columns if column not in df.columns]

        if missing_columns:
            raise DataValidationError(f"Missing columns: {missing_columns}")

    def validate_target_column(self, df: pd.DataFrame) -> None:
        """
        Validate target column exists.
        """

        logger.info("Checking target column.")

        target_column = self.schema["target"]

        if target_column not in df.columns:
            raise DataValidationError(f"Target column '{target_column}' not found.")

    def validate_missing_values(self, df: pd.DataFrame) -> None:
        """
        Check for NULL values and blank string values.

        Note:
            Some datasets contain empty strings instead of NaN values.
        """

        logger.info("Checking missing values.")

        # Check actual NULL values
        null_values = df.isnull().sum()

        if null_values.any():
            logger.warning(f"Found NULL values:\n{null_values[null_values > 0]}")

        # Check blank strings in object columns
        blank_values = df.select_dtypes(include=["object"]).apply(
            lambda column: column.str.strip().eq("").sum()
        )

        if blank_values.any():
            logger.warning(f"Found blank string values:\n{blank_values[blank_values > 0]}")

    def validate_duplicates(self, df: pd.DataFrame) -> None:
        """
        Check duplicate records.
        """

        logger.info("Checking duplicate records.")

        duplicate_count = df.duplicated().sum()

        if duplicate_count > 0:
            logger.warning(f"Found {duplicate_count} duplicate rows.")
