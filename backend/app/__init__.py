from flask import Flask
from flask_cors import CORS
from flask_httpauth import HTTPTokenAuth
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()
http_auth = HTTPTokenAuth("Bearer")


def create_app(config_name):
    app = Flask(__name__)
    CORS(
        app,
        resources={
            r"/*": {"origins": [r"http://localhost:*", r"http://192.168.0.11:*"]}
        },
    )
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # call init_app to complete initialization
    db.init_app(app)

    # create app blueprints
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    from .payments import payments as payments_blueprint

    app.register_blueprint(payments_blueprint, url_prefix="/payments")

    from .users import users as users_blueprint

    app.register_blueprint(users_blueprint, url_prefix="/users")

    from .items import items as items_blueprint

    app.register_blueprint(items_blueprint, url_prefix="/items")

    return app
