from os import environ
from flask import Flask
from logic.database import Database

# connection to database that is accessible by other parts of the application
mysql_db = Database()

def create_app():
    app = Flask(__name__)
    
    # Config for generating form hidden tags
    app.config['SECRET_KEY'] = environ.get('SECRET_KEY') 

    # Database config information all data located in env variables
    # Currently needs to be housed locally will be placed in distributions os env
    # Depreciated 'logic/database.py'
    # app.config['MYSQL_HOST'] = environ.get('MYSQL_HOST')
    # app.config['MYSQL_USER'] = environ.get('MYSQL_USER')
    # app.config['MYSQL_PASSWORD'] = environ.get('MYSQL_PASSWORD')
    # app.config['MYSQL_DB'] = environ.get('MYSQL_DB')
    
    # Blueprints are registered and are incorporated into the app
    from routes.common_routes import common
    app.register_blueprint(common)

    from routes.auth_routes import auth
    app.register_blueprint(auth)

    # returns our app so that it my be accessed by other pieces of the app
    return app
