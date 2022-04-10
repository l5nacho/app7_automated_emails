from app import app, db
from flask import render_template, flash, url_for, redirect, get_flashed_messages, make_response, request, session
from models import User
from datetime import datetime

import forms
import json


@app.route('/')
def home():
    return '<h1>Carrusel de imagenes estaticas</h1>'

@app.route('/index')
def index():
    # custom_cookie = request.cookies.get('custom_cookie', 'undefined')
    # print(custom_cookie)
    if 'username' in session:
        username = session['username']
        print(username)
    users = User.query.all()
    return render_template('index.html',
                           users=users)

@app.route('/cookie')
def cookie():
    response = make_response('<h1>Cookies</h1>')
    response.set_cookie('custom_cookie', 'Nacho')
    return response


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.AddUserForm()
    if form.validate_on_submit():
        user = User(name=form.name.data,
                    email=form.email.data,
                    topic=form.topic.data,
                    date_add=datetime.utcnow(),
                    date_mod=datetime.utcnow())
        db.session.add(user)
        db.session.commit()
        print(f'data added {user.name} {user.email} {user.topic}')
        flash('User added to the database')
        return redirect(url_for('index'))
    return render_template('register.html',
                           form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = forms.loginForm()
    if request.method == 'POST' and login_form.validate():
        session['username'] = login_form.user.data
    return render_template('login.html',
                           form=login_form)

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))

@app.route('/ajax-login', methods=['POST'])
def ajax_login():
    username = request.form['username']
    response = {'status': 200, 'username': username, 'id': 1}
    return json.dumps(response)
