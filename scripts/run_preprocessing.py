import pandas as pd

from customer_churn_mlops.common.logger import logger
from customer_churn_mlops.common.paths import TRAIN_DATA_PATH
from customer_churn_mlops.training.preprocessor import (
    PreprocessorTrainer,
)


def main():
    logger.info("Loading training dataset...")

    train_df = pd.read_csv(TRAIN_DATA_PATH)

    trainer = PreprocessorTrainer()

    X_train, y_train = trainer.fit_transform(train_df)

    logger.info(f"Processed feature shape : {X_train.shape}")
    logger.info(f"Target shape            : {y_train.shape}")


if __name__ == "__main__":
    main()
