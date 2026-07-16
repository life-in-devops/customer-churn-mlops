from customer_churn_mlops.data.ingestion import DataIngestion
from customer_churn_mlops.data.validation import DataValidation

ingestion = DataIngestion()
validator = DataValidation()

df = ingestion.ingest()

validator.validate(df)

print("Validation Successful!")
