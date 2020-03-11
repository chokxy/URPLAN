
from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm

@app.route('/home', methods=['GET', 'POST'])
def home():
    user = {'username': 'Chok'}
    if request.method == 'POST':
        days=request.form.getlist('days')
        # database querying
        return render_template('termplan.html', days=days)
    return render_template('home.html', title='Home', user=user)

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('hello.html', form=form)

# if __name__ == '__main__':
app.run(debug=True)