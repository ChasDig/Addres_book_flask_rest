import os
from pathlib import Path

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
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR.joinpath('application.db').as_posix()}"


class ProductionConfig(BaseConfig):
    """Additional configurations for the application when production."""
    pass


class ApplicationConfig:
    """Setting configurations for the application."""
    @staticmethod
    def configuration_setting(configuration_type: str):
        match configuration_type:
            case "testing":
                return TestConfig
            case "develop":
                return ProductionConfig
        return "Error!"


config = ApplicationConfig.configuration_setting("testing")
