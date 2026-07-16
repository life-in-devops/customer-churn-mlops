from customer_churn_mlops.data.ingestion import DataIngestion
from customer_churn_mlops.data.splitter import DataSplitter
from customer_churn_mlops.data.validation import DataValidation


def main() -> None:
    ingestion = DataIngestion()
    validator = DataValidation()
    splitter = DataSplitter()

    df = ingestion.ingest()

    validator.validate(df)

    train_df, test_df = splitter.split(df)

    splitter.save(train_df, test_df)


if __name__ == "__main__":
    main()
