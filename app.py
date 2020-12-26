from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret'

login_manager = LoginManager(app)

if __name__ == "__main__":
    app.run(debug=True)
