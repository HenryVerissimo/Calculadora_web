from flask import Flask
from app.config.app_configs import flask_configs


def create_app(config_name="DEVELOPMENT") -> Flask:
    """
        Make and configure new Flask application

        params:
            - config_name: Name of the configuration chosen in flask_configs

        return: Flask app instance
    """

    app = Flask(__name__)

    app.config.from_object(flask_configs.get(config_name.upper(), flask_configs["DEVELOPMENT"]))

    return app