

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nogame.db'
app.secret_key = 'Hellough'
db = SQLAlchemy(app)

from nogame import models
from nogame import views
from nogame import admin