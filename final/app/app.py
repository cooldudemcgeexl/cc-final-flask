import os

from flask import Flask
from flask_login import LoginManager

from ..blueprints import auth, data, root, test
from ..constants import POSTGRES_CON_STR
from ..models import *
from .database import db


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    
    app.secret_key = os.urandom(24) #TODO: Change me
    app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES_CON_STR

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    app.register_blueprint(root)
    app.register_blueprint(auth)
    app.register_blueprint(test)
    app.register_blueprint(data)

    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    return app