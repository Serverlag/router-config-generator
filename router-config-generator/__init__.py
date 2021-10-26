import flask
import os

SECRET_KEY = os.urandom(32)

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY