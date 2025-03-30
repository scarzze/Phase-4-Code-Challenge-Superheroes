from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db  # Import our SQLAlchemy instance
from .routes import api_bp  # Import our API blueprint

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # -----------------------------
    # CONFIGURATION
    # -----------------------------
    # Set up database URI and disable modification tracking for performance.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # -----------------------------
    # INITIALIZE EXTENSIONS
    # -----------------------------
    # Initialize the SQLAlchemy database with our app.
    db.init_app(app)

    # Set up Flask-Migrate to handle database migrations.
    Migrate(app, db)

    # -----------------------------
    # REGISTER BLUEPRINTS
    # -----------------------------
    # Register our API blueprint which contains all our routes.
    app.register_blueprint(api_bp)

    return app
