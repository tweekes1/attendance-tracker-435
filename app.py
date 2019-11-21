from flask import Flask
from flaskext.mysql import MySQL
from os import environ


def create_app():
    app = Flask(__name__)
    
    # Config for generating form hidden tags
    app.config['SECRET_KEY'] = environ.get('SECRET_KEY') 

    # Database config information all data located in env variables
    # Currently needs to be housed locally will be placed in distributions os env
    app.config['MYSQL_HOST'] = environ.get('MYSQL_HOST')
    app.config['MYSQL_USER'] = environ.get('MYSQL_USER')
    app.config['MYSQL_PASSWORD'] = environ.get('MYSQL_PASSWORD')
    app.config['MYSQL_DB'] = environ.get('MYSQL_DB')
    
    # Blueprints are registered and are incorporated into the app
    from routes.common_routes import common
    app.register_blueprint(common)

    from routes.auth_routes import auth
    app.register_blueprint(auth)

    # returns our app so that it my be accessed by other pieces of the app
    return app

# Main components of the app. The app itself and the database connecting to the app
app = create_app()
mysql = MySQL(app)