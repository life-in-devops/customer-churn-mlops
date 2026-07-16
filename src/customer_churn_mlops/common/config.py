from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------
    app_name: str = Field(default="customer-churn-mlops")
    app_env: str = Field(default="development")
    app_version: str = Field(default="0.1.0")

    # ------------------------------------------------------------------
    # Logging
    # ------------------------------------------------------------------
    log_level: str = Field(default="INFO")

    # ------------------------------------------------------------------
    # MLflow
    # ------------------------------------------------------------------
    mlflow_host: str = Field(default="localhost")
    mlflow_port: int = Field(default=5000)

    # ------------------------------------------------------------------
    # AWS
    # ------------------------------------------------------------------
    aws_region: str = Field(default="ap-south-1")

    # ------------------------------------------------------------------
    # API
    # ------------------------------------------------------------------
    api_host: str = Field(default="0.0.0.0")
    api_port: int = Field(default=8000)

    @property
    def mlflow_tracking_uri(self) -> str:
        return f"http://{self.mlflow_host}:{self.mlflow_port}"


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached Settings instance.
    """
    return Settings()


settings = get_settings()
