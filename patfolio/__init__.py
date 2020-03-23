from flask import Flask, redirect, url_for
from flask_admin import Admin, AdminIndexView
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'changemeforproduction'

login_manager = LoginManager(app)

db = SQLAlchemy(app)


from patfolio import routes
from patfolio.models import User


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))


admin = Admin(app, name='Admin Console', index_view=MyAdminIndexView())
admin.add_view(ModelView(User, db.session))
