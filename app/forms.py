from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Length(max=150)])
    password = PasswordField("Senha", validators=[DataRequired(), Length(max=150)])
    submit = SubmitField("Entrar")


class RegisterForm(FlaskForm):
    username = StringField(
        "Nome de usuário", validators=[DataRequired(), Length(max=150)]
    )
    email = EmailField("Email", validators=[DataRequired(), Length(max=150)])
    password = PasswordField("Senha", validators=[DataRequired(), Length(max=150)])
    submit = SubmitField("Criar Conta")
