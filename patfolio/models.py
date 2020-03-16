from patfolio import db
from patfolio import login_manager


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return 'User: ' + self.username


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)