"""
CareerGPS India Application Factory
"""

from flask import Flask
from app.models import User
from config import Config
from extensions import (
    db,
    login_manager,
    migrate
)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    """
    Create and configure the Flask application.
    """

    app = Flask(__name__)

    app.config.from_object(Config)

    # Import models so Flask-Migrate can detect them
    from app.models import User

    # Initialize database
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Initialize login manager
    login_manager.init_app(app)

    # Configure login route
    login_manager.login_view = "main.login"
    
    # Initialize migrations
    migrate.init_app(app, db)

    from app.routes import main
    app.register_blueprint(main)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app