from customer_churn_mlops.data.ingestion import DataIngestion

ingestion = DataIngestion()

df = ingestion.ingest()

print(df.head())

print(df.shape)
