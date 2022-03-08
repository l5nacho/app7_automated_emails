from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddUserForm(FlaskForm):
    name = StringField('Name: ')
    email = StringField('Email: ')
    topic = StringField('Topic: ')
    submit = SubmitField('Register')
