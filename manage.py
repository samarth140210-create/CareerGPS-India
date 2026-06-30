"""
CareerGPS India Migration Manager
"""

from app import create_app
from extensions import db

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db
    }