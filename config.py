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

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///careergps.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    APP_NAME = os.getenv(
        "APP_NAME",
        "CareerGPS India"
    )

    APP_VERSION = os.getenv(
        "APP_VERSION",
        "1.0.0"
    )