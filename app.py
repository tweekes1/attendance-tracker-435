from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Index")

@app.route("/register")
def register():
    return render_template("register.html", title="Registration")

# @app.route("/register", methods=['POST'])
# def register_post():
#     return render_template("index.html")

# @app.route("/login")
# def login():
#     return render_template("login.html", title="Login")

# @app.route("/login", methods=['POST'])
# def login_post():
    # return render_template("index.html")
