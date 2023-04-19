import os

from flask import Flask
from flask_login import LoginManager

from ..blueprints import auth, root
from ..constants import POSTGRES_PWD
from ..models import *
from .database import db


def create_app():
    app = Flask(__name__, template_folder='../templates')
    
    app.secret_key = os.urandom(24) #TODO: Change me
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://cc_postgres_admin:{POSTGRES_PWD}@cc-final-postgres2.postgres.database.azure.com/postgres?sslmode=require'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    app.register_blueprint(root)
    app.register_blueprint(auth)

    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    return app