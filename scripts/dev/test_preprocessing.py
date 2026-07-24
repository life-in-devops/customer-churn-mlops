import pandas as pd

from customer_churn_mlops.features.preprocessing import DataPreprocessor

df = pd.read_csv("data/raw/customer_churn.csv")

print("Before Cleaning")
print(df.dtypes)
print(df.head())

clean_df = DataPreprocessor.clean(df)

print("\nAfter Cleaning")
print(clean_df.dtypes)
print(clean_df.head())

print("\nMissing Values")
print(clean_df.isnull().sum())
