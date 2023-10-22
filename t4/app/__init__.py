from flask import Flask
from app.config import SECRET_KEY, CSRF_ENABLED

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/postgres'
app.config['SECRET_KEY'] = SECRET_KEY
app.config['CSRF_ENABLED'] = CSRF_ENABLED

from app import views