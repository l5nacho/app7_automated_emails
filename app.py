from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

csrf = CSRFProtect(app)
db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)