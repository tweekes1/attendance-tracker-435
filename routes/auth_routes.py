from app import mysql_db
from forms import LoginForm, RegistrationForm
from flask import Blueprint, redirect, render_template, request, url_for
from werkzeug.security import check_password_hash, generate_password_hash

# Blueprint that will register 'auth' or authentication routes
# Routes that will require user authentication or depend on 
# user authentication
auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():

            user = mysql_db.get_existing_user(form.email.data)
            
            if not user or not check_password_hash(user['password_hash'], form.password.data):
                # User login in fails tell them it failed and send them back to login page
                return redirect(url_for('auth.login'))
            else:
                # If login successful send them to profile page
                # sends to index for now
                return redirect(url_for('common.index'))


    return render_template('login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            
            user_exists = mysql_db.user_exists(form.email.data)
            
            if user_exists:
                # if there exists a user with that email tell them their account exists
                # and send them to the login page
                return redirect(url_for('auth.login'))

            pw_hash = generate_password_hash(form.password.data)
            mysql_db.create_user(form.name.data, form.email.data, pw_hash, request.form['user_type'])

            return render_template('index.html')

    return render_template('register.html', form=form)

@auth.route('/logout')
def logout():
    return render_template('logout.html', title='Logout')