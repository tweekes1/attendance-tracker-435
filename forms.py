from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Required 

# Forms that will be used for our site. More may need to be added they should go here
# To keep code clean and organized

class LoginForm(FlaskForm):
    email = StringField('Email', 
                        [DataRequired(), Email(), Length(min=5, max=90), Required()])
    password = PasswordField('Password', 
                        [DataRequired(), Length(min=8, max=25), Required()])
    login_btn = SubmitField('Login')

class RegistrationForm(FlaskForm):
    # Removed netid parameter since this will not be used primarily for hunter student
    # netid = StringField('Netid', [DataRequired(), Length(min=5, max=10), DataRequired()])
    name = StringField('Name', [DataRequired(), Length(min=3, max=50), Required()])
    email = StringField('Email', [DataRequired(), Email(), Required()])
    password = PasswordField('Password', [DataRequired(), Length(min=8, max=25, message="Password should have a length of 8-25 characters"), Required()])
    confirm_password = PasswordField('Confirm Password', [EqualTo('password', message="Passwords must match"), Required()])
    submit_btn = SubmitField('Submit')
