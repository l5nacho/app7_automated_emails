from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms import validators

class AddUserForm(FlaskForm):
    name = StringField('Name: ',
                       [validators.InputRequired(message='Por favor ingrese un nombre')])
    user = StringField('Usuario',
                       [validators.InputRequired(message='Por favor ingrese un usuario')])
    password = PasswordField('Contraseña')
    email = StringField('Email: ',
                        [validators.InputRequired(message='Por favor ingrese un email'),
                         validators.Email(message='Ingrese un email valido')])
    topic = StringField('Topic: ',
                        [validators.InputRequired(message='Ingrese un tema')])
    submit = SubmitField('Register')

class loginForm(FlaskForm):
    user = StringField('Usuario',
                       [validators.InputRequired(message='Por favor ingrese un usuario')],
                       render_kw={'placeholder': 'Introduce el Usuario'})
    password = PasswordField('Contraseña', render_kw={'placeholder': 'Introduce la contraseña'})
    submit = SubmitField('Login')