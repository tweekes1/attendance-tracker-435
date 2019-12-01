from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Required 

# Forms that will be used for our site. More may need to be added they should go here
# To keep code clean and organized

class LoginForm(FlaskForm):
    email = StringField('Email', 
                        [DataRequired(), Email(message='Please enter a valid email address'), Length(min=5, max=90), Required()])
    password = PasswordField('Password', 
                        [DataRequired(), Length(min=8, max=25, message='Invalid Password'), Required()])
    login_btn = SubmitField('Login')

class RegistrationForm(FlaskForm):
    name = StringField('Name', [DataRequired(), Length(min=3, max=50), Required()])
    email = StringField('Email', [DataRequired(), Email(message='Please enter a valid email address')])
    password = PasswordField('Password', [DataRequired(), Length(min=8, max=25, message='Password should have a length of 8-25 characters'), 
                                Required()])
    confirm_password = PasswordField('Confirm Password', [DataRequired(), EqualTo('password', message='Passwords must match')])
    submit_btn = SubmitField('Submit')
