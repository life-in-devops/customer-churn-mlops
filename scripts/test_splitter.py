from customer_churn_mlops.data.ingestion import DataIngestion
from customer_churn_mlops.data.splitter import DataSplitter
from customer_churn_mlops.data.validation import DataValidation

ingestion = DataIngestion()
validator = DataValidation()
splitter = DataSplitter()


df = ingestion.ingest()

validator.validate(df)

train_df, test_df = splitter.split(df)

splitter.save(
    train_df,
    test_df,
)


print("Train dataset:")
print(train_df.shape)

print()

print("Test dataset:")
print(test_df.shape)
