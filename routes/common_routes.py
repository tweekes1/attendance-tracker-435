from flask import Blueprint, redirect, render_template

# Blueprint that will be used to register new common routes for the app
# common = does not need authentication can be accessed regardless of login
common = Blueprint('common', __name__, template_folder='templates')

@common.route('/')
@common.route('/home')
@common.route('/index')
def index():
    return render_template('index.html', title='Home')

@common.route('/about')
def about():
    return render_template('about.html', title='About')