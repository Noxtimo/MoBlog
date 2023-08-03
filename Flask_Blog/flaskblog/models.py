from flaskblog import db, login_manager, app
from datetime import datetime
from flask_login import UserMixin
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer

@login_manager.user_loader
def load_user(user):
    return User.query.get(user)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default='default.jpeg')
    post = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self):
        s = Serializer(app.secret_key)
        return s.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.secret_key)
        try:
            user_id = s.loads(token, max_age=1800)['user_id']
            print(user_id)
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}'), '{self.email}'), '{self.image_file}')"



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.String(120), db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}'), '{self.date_posted}')"