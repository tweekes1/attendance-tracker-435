from flask import Blueprint, redirect, render_template, request
from forms import LoginForm, RegistrationForm

# Blueprint that will register 'auth' or authentication routes
# Routes that will require user authentication or depend on 
# user authentication
auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        print('hello')
        if form.validate_on_submit():
            # STUB
            # Check to make sure that the user exists and if there password is correct
            # If they don't Flash message
            return render_template('index.html')
            
    return render_template('login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            # STUB
            # Check to make sure the user doesn't exist already
            # if they do flash message if they dont add them to 
            # user database

            return render_template('index.html')
            
    return render_template('register.html', form=form)

@auth.route('/logout')
def logout():
    return render_template('logout.html', title='Logout')