from flask import Flask 
from .config import Config
from app.models import db, Book

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
Migrate(app, db) #investigate

