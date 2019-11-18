from flask import Blueprint, redirect, render_template
from forms import LoginForm, RegistrationForm

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    return render_template('login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    return render_template('register.html', form=form)

@auth.route('/logout')
def logout():
    return render_template('logout.html', title='Logout')