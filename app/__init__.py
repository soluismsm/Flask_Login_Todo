import os

from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


bootstrap = Bootstrap5()
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_file=None):
    app = Flask(__name__, instance_relative_config=True)

    if config_file is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_object(config_file)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .views import views
    from .auth import auth

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(views)
    app.register_blueprint(auth)

    with app.app_context():
        db.create_all()

    return app
