from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Environment
from datetime import datetime

app = Flask(__name__, template_folder='templates')
app.config.from_object('app.config.Config')

db = SQLAlchemy(app)

from app.views import views