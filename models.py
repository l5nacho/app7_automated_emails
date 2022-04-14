from app import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(66), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    date_add = db.Column(db.Date, nullable=False)
    date_mod = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return(f'Hola {self.name} Usuario {self.user} con email {self.email} '
               f'ha sido creado el {self.date_add}')

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(66), nullable=False)

    def __repr__(self):
        return f'Usuario {self.username} ha sido creado el {self.date_created}'
