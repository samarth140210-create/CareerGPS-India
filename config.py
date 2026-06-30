"""
CareerGPS India Configuration

This file contains all application configuration
settings loaded from environment variables.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Config:
    """
    Base configuration class.
    """

    SECRET_KEY = os.getenv("SECRET_KEY")

    database_url = os.getenv("DATABASE_URL")

    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace(
            "postgres://",
            "postgresql://",
            1
        )

    SQLALCHEMY_DATABASE_URI = (
        database_url
        or
        "sqlite:///careergps.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    APP_NAME = os.getenv(
        "APP_NAME",
        "CareerGPS India"
    )

    APP_VERSION = os.getenv(
        "APP_VERSION",
        "1.0.0"
    )