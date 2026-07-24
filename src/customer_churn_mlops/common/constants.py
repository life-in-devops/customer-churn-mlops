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

LOGISTIC_REGRESSION = "logistic_regression"
RANDOM_FOREST = "random_forest"
GRADIENT_BOOSTING = "gradient_boosting"

PRIMARY_METRIC = "roc_auc"

ACCURACY = "accuracy"
PRECISION = "precision"
RECALL = "recall"
F1_SCORE = "f1_score"
ROC_AUC = "roc_auc"

METRICS_FILE = "metrics.json"
MODEL_METADATA_FILE = "model_metadata.json"
