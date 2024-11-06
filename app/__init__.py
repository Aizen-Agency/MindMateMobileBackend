# __init__.py

from flask import Flask
from .config import Config
from .models import db, User
from .routes import auth_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config.from_object(db)
    app.config.from_object(User)
    app.config.from_object(auth_blueprint)
    
    # Initialize other parts of the app (e.g., blueprints, databases)
    
    return app
