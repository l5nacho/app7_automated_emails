from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    date_add = db.Column(db.Date, nullable=False)
    date_mod = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return(f'Usuario {self.name} con email {self.email} '
               f'ha sido creado el {self.date_add}')

class Username(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.column(db.String(20), unique=True)
    password = db.column(db.String(66))
    date_created = db.column(db.Date)