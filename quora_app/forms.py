from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo ,ValidationError
from quora_app import app,db
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        username = username.data
        conn = db.connect()
        cursor =conn.cursor()
        cursor.execute("SELECT username FROM user WHERE username = (%s)",(username))
        user = cursor.fetchone()
        if user:
            raise ValidationError('Username Already Exits')

    def validate_email(self,email):
        email = email.data
        conn = db.connect()
        cursor =conn.cursor()
        cursor.execute("SELECT email FROM user WHERE email = (%s)",(email))
        emailId = cursor.fetchone()
        if emailId:
            raise ValidationError('Email Address Already Exits')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
