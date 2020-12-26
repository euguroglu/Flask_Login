from flask import Flask
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager(app)
db = SQLAlchemy(app)


class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),unique=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
#or return User.query.filter_by(id=int(user_d))

@app.route('/login')
def login():
    user = User.query.filter_by(username='enes').first()
    login_user(user)
    return '<h1>Logged in</h1>'

@app.route('/home')
@login_required
def home():
    return '<h1>You are in the protected area, {}</h1>'.format(current_user.username)

if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()
