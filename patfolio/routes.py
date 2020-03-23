from patfolio import app
from patfolio.forms import LoginForm
from flask import render_template, url_for, flash, redirect
from patfolio.models import User
from flask_login import logout_user, login_user


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        flash(('Login requested for user {}, remember_me={}').format(
            form.username.data, form.remember_me.data))
        return redirect('/admin')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))