from __init__ import app
import views

# TODO: #1 Move secret key to env file and load configuration to be more secure
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY