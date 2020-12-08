from flask import Flask
from flask_cors import CORS
from .database.models import setup_db, Post, Comment

app = Flask(__name__)
setup_db(app)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'
