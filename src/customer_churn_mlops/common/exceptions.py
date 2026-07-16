class MLOpsException(Exception):
    """Base exception for the project."""


class DataValidationError(MLOpsException):
    """Raised when data validation fails."""


class ModelTrainingError(MLOpsException):
    """Raised when model training fails."""


class ModelInferenceError(MLOpsException):
    """Raised during inference failures."""
