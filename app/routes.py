
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/home')
def index():
    user = {'username': 'Chok'}
    return render_template('home.html', title='Home', user=user)

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('hello.html', form=form)