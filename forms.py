from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators

class AddUserForm(FlaskForm):
    name = StringField('Name: ',
                       [validators.InputRequired(message='Por favor ingrese un nombre')])
    email = StringField('Email: ',
                        [validators.InputRequired(message='Por favor ingrese un email'),
                         validators.Email(message='Ingrese un email valido')])
    topic = StringField('Topic: ',
                        [validators.InputRequired(message='Ingrese un tema')])
    submit = SubmitField('Register')
