from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators

class AddUserForm(FlaskForm):
    name = StringField('Name: ',
                       [validators.DataRequired(message='Por favor ingrese un nombre')])
    email = StringField('Email: ',
                        [validators.DataRequired(message='Por favor ingrese un email'),
                         validators.Email(message='Ingrese un email valido')])
    topic = StringField('Topic: ',
                        [validators.DataRequired(message='Ingrese un tema')])
    submit = SubmitField('Register')
