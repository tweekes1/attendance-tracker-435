from os import environ
from flask import Flask, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .database import Database

# connection to database that is accessible by other parts of the application
# mysql_db = Database()
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    
    # Config for generating form hidden tags
    app.config['SECRET_KEY'] = environ.get('SECRET_KEY') 
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initializes all necessary items for app to function
    with app.app_context():
        from .auth_routes import auth
        from .common_routes import common

        app.register_blueprint(auth)
        app.register_blueprint(common)

        db.init_app(app)
        login_manager.init_app(app)
        login_manager.login_view = 'auth.login'
    
    return app