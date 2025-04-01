from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create SQLAlchemy instance
db = SQLAlchemy()

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'  # Use SQLite database file
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)
    
    # Register blueprints
    from .routes import api_bp  # Import our routes blueprint
    app.register_blueprint(api_bp)
    
    return app
