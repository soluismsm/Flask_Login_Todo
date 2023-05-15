from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Length(max=150)])
    password = PasswordField("Password", validators=[DataRequired(), Length(max=150)])
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(max=150)])
    email = EmailField("Email", validators=[DataRequired(), Length(max=150)])
    password = PasswordField("Password", validators=[DataRequired(), Length(max=150)])
    submit = SubmitField("Sign up")
