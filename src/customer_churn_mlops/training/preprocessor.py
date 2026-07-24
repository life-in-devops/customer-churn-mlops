import json

import joblib
import pandas as pd

from customer_churn_mlops.common.constants import TARGET_COLUMN
from customer_churn_mlops.common.logger import logger
from customer_churn_mlops.common.paths import (
    FEATURE_NAMES_PATH,
    PREPROCESSOR_PATH,
)
from customer_churn_mlops.features.pipeline import (
    create_preprocessing_pipeline,
)
from customer_churn_mlops.features.preprocessing import (
    DataPreprocessor,
)


class PreprocessorTrainer:
    """
    Fits and saves the preprocessing pipeline.
    """

    def __init__(self):
        self.pipeline = create_preprocessing_pipeline()

    def fit_transform(self, train_df: pd.DataFrame):
        """
        Fit preprocessing pipeline and transform training data.
        """

        logger.info("Cleaning training dataset...")

        train_df = DataPreprocessor.clean(train_df)

        X_train = train_df.drop(columns=[TARGET_COLUMN])
        y_train = train_df[TARGET_COLUMN]

        logger.info("Fitting preprocessing pipeline...")

        X_train_processed = self.pipeline.fit_transform(X_train)

        logger.info("Saving preprocessing pipeline...")

        joblib.dump(self.pipeline, PREPROCESSOR_PATH)

        logger.info(f"Preprocessor saved to {PREPROCESSOR_PATH}")

        feature_names = self.pipeline.get_feature_names_out().tolist()

        with open(FEATURE_NAMES_PATH, "w") as fp:
            json.dump(feature_names, fp, indent=4)

        logger.info(f"Feature names saved to {FEATURE_NAMES_PATH}")

        return X_train_processed, y_train
