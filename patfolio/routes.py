from patfolio import app
from patfolio.forms import LoginForm
from flask import render_template, url_for, flash, redirect


@app.route('/')
def hello():
    return render_template('base.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(('Login requested for user {}, remember_me={}').format(
            form.username.data, form.remember_me.data))
        return redirect('/admin')
    return render_template('login.html', title='Sign In', form=form)
