from os import getenv
from dotenv import load_dotenv


load_dotenv()

class BaseConfig:
    """ Base configuration for Flask application"""

    TESTING = False
    DEBUG = False
    TEMPLATES_AUTO_RELOAD = False

class DevelopmentConfig(BaseConfig):
    """ Development configuration """

    SECRET_KEY = getenv("DEV_SECRET", "default_secret")
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True

class TestingConfig(BaseConfig):
    """ Testing configuration """

    SECRET_KEY = getenv("TEST_SECRET", "default_secret")
    DEBUG = True
    TESTING = True

class ProductionConfig(BaseConfig):
    """ Production configuration """

    SECRET_KEY = getenv("SECRET_KEY")

    

flask_configs = {
    "DEVELOPMENT": DevelopmentConfig(),
    "TESTING": TestingConfig(),
    "PRODUCTION": ProductionConfig()
}
