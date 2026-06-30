"""
CareerGPS India Database Models
"""

from flask_login import UserMixin
from datetime import datetime
from extensions import db


class User(UserMixin, db.Model):
    """
    User account model.
    """

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    full_name = db.Column(
        db.String(150),
        nullable=False
    )

    email = db.Column(
        db.String(255),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    is_admin = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def __repr__(self):
        return f"<User {self.email}>"
    
class CareerAssessment(db.Model):
    """
    Career assessment results.
    """

    __tablename__ = "career_assessments"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    science_score = db.Column(
        db.Integer,
        default=0
    )

    commerce_score = db.Column(
        db.Integer,
        default=0
    )

    arts_score = db.Column(
        db.Integer,
        default=0
    )

    technology_score = db.Column(
        db.Integer,
        default=0
    )

    leadership_score = db.Column(
        db.Integer,
        default=0
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def __repr__(self):
        return (
            f"<CareerAssessment "
            f"{self.id}>"
        )
    
class StudentProfile(db.Model):
    """
    Student profile model.
    """

    __tablename__ = "student_profiles"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    education_level = db.Column(
        db.String(50)
    )

    current_class = db.Column(
        db.String(20)
    )

    stream = db.Column(
        db.String(50)
    )

    degree = db.Column(
        db.String(100)
    )

    twelfth_percentage = db.Column(
        db.Float
    )

    passions = db.Column(
        db.Text
    )

    skills = db.Column(
        db.Text
    )

    dream_job = db.Column(
        db.String(255)
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    updated_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        onupdate=db.func.now()
    )

    def __repr__(self):
        return (
            f"<StudentProfile {self.user_id}>"
        )
    
class CareerMission(db.Model):

    __tablename__ = "career_missions"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    career_name = db.Column(
        db.String(255),
        nullable=False
    )

    completed = db.Column(
        db.Boolean,
        default=False
    )

    completed_at = db.Column(
        db.DateTime,
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

class CompletedMission(db.Model):

    __tablename__ = "completed_missions"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    career_name = db.Column(
        db.String(255),
        nullable=False
    )

    completed_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

class MissionProgress(db.Model):

    __tablename__ = "mission_progress"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id"
        ),
        nullable=False
    )

    mission_name = db.Column(
        db.String(255),
        nullable=False
    )

    month = db.Column(
        db.String(50),
        nullable=False
    )

    week = db.Column(
        db.String(50),
        nullable=False
    )

    task_name = db.Column(
        db.String(255),
        nullable=False
    )

    completed = db.Column(
        db.Boolean,
        default=False
    )

class WeekCompletion(db.Model):

    __tablename__ = "week_completion"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "users.id"
        ),
        nullable=False
    )

    mission_name = db.Column(
        db.String(255),
        nullable=False
    )

    month = db.Column(
        db.String(50),
        nullable=False
    )

    week = db.Column(
        db.String(50),
        nullable=False
    )

    completed = db.Column(
        db.Boolean,
        default=False
    )

    completed_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )