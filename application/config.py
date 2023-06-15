import os
from pathlib import Path
from typing import Type
from sqlalchemy import create_engine

BASE_DIR = Path(__file__).resolve().parent.parent


class BaseConfig:
    """Base config for application."""
    SECRET_KEY = "2URRNdKXwuDw6ErOMzGk"
    REST_X_JSON = {
        "ensure_ascii": False,
    }


class TestConfig(BaseConfig):
    """Additional configurations for the application when testing."""
    TESTING = True
    DEBUG = True
    SQLALCHEMY_ECHO = True
    DATA_BASE_NAME = "application.db"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR.joinpath(DATA_BASE_NAME).as_posix()}"


class ProductionConfig(BaseConfig):
    """Additional configurations for the application when production."""
    DEBUG = False
    SQLALCHEMY_ECHO = True
    USERNAME = "postgres"
    PASSWORD = "postgres"
    HOST = "172.18.0.2"
    PORT = 5432
    DATA_BASE_NAME = "postgres"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATA_BASE_NAME}"


class ApplicationConfig:
    """Setting configurations for the application."""
    @staticmethod
    def configuration_setting(configuration_type: str) -> Type[BaseConfig] | str:
        match configuration_type:
            case "testing":
                return TestConfig
            case "develop":
                return ProductionConfig
        return "Error!"


config = ApplicationConfig.configuration_setting("develop")
engine = create_engine(TestConfig.SQLALCHEMY_DATABASE_URI)

