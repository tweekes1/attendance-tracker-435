from os import environ
from flask import Flask, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from logic.database import Database

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

    # Blueprints are registered and are incorporated into the app
    from routes.common_routes import common
    app.register_blueprint(common)

    from routes.auth_routes import auth
    app.register_blueprint(auth)

    # Initializes all necessary items for app to function
    with app.app_context():
        db.init_app(app)
        login_manager.init_app(app)
        login_manager.login_view = 'auth.login'
    
    return app