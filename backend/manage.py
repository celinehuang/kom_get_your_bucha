#!/usr/bin/env python
import os

# from app.models import User, Role
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# Import settings from .env file. Must define FLASK_CONFIG
if os.path.exists(".env"):
    print("Importing environment from .env file")
    for line in open(".env"):
        var = line.strip().split("=")
        if len(var) == 2:
            os.environ[var[0]] = var[1]

from app import create_app, db

manager = Manager(create_app)
# e.g. "python manage.py --config development runserver"
manager.add_option("-c", "--config", dest="config_name", required=False)


# app = create_app(os.getenv("FLASK_CONFIG") or "default")
# migrate = Migrate(app, db)


# @manager.command
# def test():
#     """Run the unit tests."""
#     import unittest

#     tests = unittest.TestLoader().discover("tests")
#     unittest.TextTestRunner(verbosity=2).run(tests)


# @manager.command
# def behave():
#     """Run the behave tests."""
#     os.system("behave")


@manager.command
def recreate_db():
    db.drop_all()
    db.create_all()


manager.add_command("db", MigrateCommand)
if __name__ == "__main__":
    manager.run()
