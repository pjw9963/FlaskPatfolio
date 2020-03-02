from flask import Flask
from flask_admin import Admin, AdminIndexView
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


from patfolio import routes
from patfolio.models import User


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return False


admin = Admin(app, name='Admin Console', index_view=MyAdminIndexView())

admin.add_view(ModelView(User, db.session))