from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Netid', 
                        validators=[DataRequired(), Email(), Length(min=5, max=10)])
    password = PasswordField('Password', 
                             validators=[DataRequired(), Length(min=8, max=25)])
    login_btn = SubmitField('Login')

class RegistrationForm(FlaskForm):
    netid = StringField('Netid', validators=[DataRequired(), Length(min=5, max=10)])
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=25)])
    confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password')])
    submit_btn = SubmitField('Submit')
