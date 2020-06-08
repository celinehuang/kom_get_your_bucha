import os

from flask import Flask
from flask_cors import CORS
from flask_httpauth import HTTPTokenAuth
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail

from config import config

db = SQLAlchemy()
migrate = Migrate()
http_auth = HTTPTokenAuth(scheme="Bearer")
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    CORS(
        app,
        resources={
            r"/*": {"origins": [r"http://localhost:*", r"http://192.168.0.11:*"]}
        },
    )
    if config_name is None:
        config_name = os.getenv("FLASK_CONFIG") or "default"

    app.config.from_object(config[config_name])
    UPLOAD_FOLDER = "{}/items/item-images".format(app.root_path)
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    config[config_name].init_app(app)

    # call init_app to complete initialization
    db.init_app(app)
    migrate.init_app(app, db)

    # set up Flask Mail extension
    mail.init_app(app)

    # create app blueprints
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    from .payments import payments as payments_blueprint

    app.register_blueprint(payments_blueprint, url_prefix="/payments")

    from .users import users as users_blueprint

    app.register_blueprint(users_blueprint, url_prefix="/users")

    from .admins import admins as admins_blueprint

    app.register_blueprint(admins_blueprint, url_prefix="/admins")

    from .items import items as items_blueprint

    app.register_blueprint(items_blueprint, url_prefix="/items")

    return app
