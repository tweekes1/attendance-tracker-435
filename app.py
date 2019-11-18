from flask import Flask

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'Big Secret'

    from routes.common_routes import common
    app.register_blueprint(common)

    from routes.auth_routes import auth
    app.register_blueprint(auth)

    return app
