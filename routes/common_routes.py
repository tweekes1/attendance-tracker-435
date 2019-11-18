from flask import Blueprint, redirect, render_template

common = Blueprint('common', __name__, template_folder='templates')

@common.route('/')
@common.route('/home')
@common.route('/index')
def index():
    return render_template('index.html', title='Home')

