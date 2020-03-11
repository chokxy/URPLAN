from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm

@app.route('/student', methods=['GET', 'POST'])
def student():
    user = {'username': 'Chok'}
    if request.method == 'POST':
        days=request.form.getlist('days')
        time=request.form.getlist('time')
        classes=request.form.get('classes')
        # database querying
        return render_template('termplan.html', days=days, time=time, classes=classes)
    return render_template('student.html', title='Home', user=user)

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('student'))
    return render_template('hello.html', form=form)

# if __name__ == '__main__':
app.run(debug=True)