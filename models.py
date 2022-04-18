from app import db
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(66), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    topic = db.relationship('Topic')
    admin = db.Column(db.Boolean, default=False)
    date_add = db.Column(db.Date, nullable=False, default=datetime.utcnow())
    date_mod = db.Column(db.Date, nullable=True, default=datetime.utcnow())

    def __repr__(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))
        # return(f'Hola {self.name} Usuario {self.username} con mail {self.email} '
        #        f'ha sido creado el {self.date_add}')

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Topic(db.Model):

    __tablename__ = 'topics'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    topic = db.Column(db.String(50), nullable=False)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(66), nullable=False)

    def __repr__(self):
        return f'Usuario {self.username} ha sido creado el {self.date_created}'
