from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('app.config')

db = SQLAlchemy(app)

with app.app_context():
    from app.routes import public_routes, admin_routes

from app.models import *
