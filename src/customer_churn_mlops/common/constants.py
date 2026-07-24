APP_NAME = "customer-churn-mlops"

DEFAULT_RANDOM_STATE = 42

TARGET_COLUMN = "Churn"
ID_COLUMN = "customerID"

TRAIN_DATASET = "train.csv"
TEST_DATASET = "test.csv"

PREPROCESSOR_NAME = "preprocessor.pkl"
MODEL_NAME = "model.pkl"

NUMERIC_FEATURES = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges",
]

CATEGORICAL_FEATURES = [
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
]

FEATURE_NAMES_FILE = "feature_names.json"
