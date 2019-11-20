from flask import Flask
from flaskext.mysql import MySQL


def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'Big Secret'

    from routes.common_routes import common
    app.register_blueprint(common)

    from routes.auth_routes import auth
    app.register_blueprint(auth)

    return app

app = create_app()
mysql = MySQL(app)