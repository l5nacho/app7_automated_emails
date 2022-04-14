from app import db
from werkzeug.security import generate_password_hash

from datetime import datetime

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(66), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    topic = db.Column(db.String(100), nullable=True)
    date_add = db.Column(db.Date, nullable=False, default=datetime.utcnow())
    date_mod = db.Column(db.Date, nullable=True, default=datetime.utcnow())

    def __init__(self, name, username, password, email, topic):
        self.name = name
        self.username = username
        self.password = self._secure_password(password)
        self.email = email
        self.topic = None


    def __repr__(self):
        return(f'Hola {self.name} Usuario {self.username} con email {self.email} '
               f'ha sido creado el {self.date_add}')

    def _secure_password(self, password):
        return generate_password_hash(password)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(66), nullable=False)

    def __repr__(self):
        return f'Usuario {self.username} ha sido creado el {self.date_created}'
