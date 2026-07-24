import pandas as pd

from customer_churn_mlops.features.pipeline import create_preprocessing_pipeline
from customer_churn_mlops.features.preprocessing import DataPreprocessor

df = pd.read_csv("data/raw/customer_churn.csv")

df = DataPreprocessor.clean(df)

X = df.drop(columns=["Churn"])

pipeline = create_preprocessing_pipeline()

pipeline.fit(X)

X_transformed = pipeline.transform(X)

print(f"Original Shape     : {X.shape}")
print(f"Transformed Shape  : {X_transformed.shape}")

print("\nPipeline Summary\n")
print(pipeline)
