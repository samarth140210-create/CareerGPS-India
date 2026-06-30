"""
CareerGPS India Flask Extensions

This file stores all Flask extension objects.

The extensions are created here and initialized
later inside the Flask Application Factory.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# Database instance
db = SQLAlchemy()

# User authentication manager
login_manager = LoginManager()

# Database migration manager
migrate = Migrate()