from patfolio import app
from flask import render_template, url_for


@app.route('/')
def hello():
    return render_template('base.html')
