"""
CareerGPS India Forms
"""

from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    SelectField,
    FloatField,
    TextAreaField,
    SelectMultipleField
)
from wtforms.widgets import CheckboxInput, ListWidget
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    Optional,
    NumberRange,
    ValidationError
)

class RegistrationForm(FlaskForm):
    """
    User registration form.
    """

    full_name = StringField(
        "Full Name",
        validators=[
            DataRequired(),
            Length(min=2, max=150)
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(),
            Length(max=255)
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8)
        ]
    )

    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo(
                "password",
                message="Passwords must match."
            )
        ]
    )

    submit = SubmitField(
        "Create Account"
    )

class LoginForm(FlaskForm):
    """
    User login form.
    """

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField(
        "Login"
    )

class AssessmentForm(FlaskForm):
    """
    Career assessment form.
    """

    science_interest = SelectField(
        "I enjoy solving scientific problems.",
        choices=[
            ("1", "Strongly Disagree"),
            ("2", "Disagree"),
            ("3", "Neutral"),
            ("4", "Agree"),
            ("5", "Strongly Agree")
        ]
    )

    commerce_interest = SelectField(
        "I enjoy business and finance activities.",
        choices=[
            ("1", "Strongly Disagree"),
            ("2", "Disagree"),
            ("3", "Neutral"),
            ("4", "Agree"),
            ("5", "Strongly Agree")
        ]
    )

    arts_interest = SelectField(
        "I enjoy creative and artistic activities.",
        choices=[
            ("1", "Strongly Disagree"),
            ("2", "Disagree"),
            ("3", "Neutral"),
            ("4", "Agree"),
            ("5", "Strongly Agree")
        ]
    )

    technology_interest = SelectField(
        "I enjoy technology and computers.",
        choices=[
            ("1", "Strongly Disagree"),
            ("2", "Disagree"),
            ("3", "Neutral"),
            ("4", "Agree"),
            ("5", "Strongly Agree")
        ]
    )

    leadership_interest = SelectField(
        "I enjoy leading teams and projects.",
        choices=[
            ("1", "Strongly Disagree"),
            ("2", "Disagree"),
            ("3", "Neutral"),
            ("4", "Agree"),
            ("5", "Strongly Agree")
        ]
    )

    submit = SubmitField(
        "Submit Assessment"
    )

class MultiCheckboxField(
    SelectMultipleField
):
    widget = ListWidget(
        prefix_label=False
    )

    option_widget = CheckboxInput()

class StudentProfileForm:
    """
    Student Profile Form
    """

class StudentProfileForm(FlaskForm):
    """
    Student Profile Form
    """

    education_level = SelectField(
        "Education Level",
        choices=[
            ("School", "School"),
            ("College", "College"),
            ("Graduate", "Graduate")
        ],
        validators=[DataRequired()]
    )

    current_class = SelectField(
        "Current Class",
        choices=[
            ("", "Select Class"),
            ("8th", "8th"),
            ("9th", "9th"),
            ("10th", "10th"),
            ("11th", "11th"),
            ("12th", "12th")
        ],
        validators=[Optional()]
    )

    stream = SelectField(
        "Stream",
        choices=[
            ("", "Select Stream"),
            ("Science", "Science"),
            ("Commerce", "Commerce"),
            ("Arts", "Arts")
        ],
        validators=[Optional()]
    )

    degree = SelectField(
        "Degree",
        choices=[
            ("", "Select Degree"),
            ("B.Tech", "B.Tech"),
            ("BCA", "BCA"),
            ("B.Sc", "B.Sc"),
            ("B.Com", "B.Com"),
            ("BBA", "BBA"),
            ("BA", "BA"),
            ("MBBS", "MBBS"),
            ("BDS", "BDS"),
            ("LLB", "LLB"),
            ("Other", "Other")
        ],
        validators=[Optional()]
    )

    twelfth_percentage = FloatField(
        "12th Percentage",
        validators=[
            Optional(),
            NumberRange(
                min=0,
                max=100
            )
        ]
    )

    passions = MultiCheckboxField(
        "Choose Your Passions",
        choices=[
            ("Programming", "Programming"), 
            ("Artificial Intelligence", "Artificial Intelligence"), 
            ("Cybersecurity", "Cybersecurity"), 
            ("Data Science", "Data Science"), 
            ("Business", "Business"), 
            ("Finance", "Finance"), 
            ("Marketing", "Marketing"), 
            ("Design", "Design"), 
            ("Writing", "Writing"), 
            ("Medicine", "Medicine"), 
            ("Engineering", "Engineering"), 
            ("Law", "Law"), 
            ("Teaching", "Teaching"), 
            ("Research", "Research"), 
            ("Government Jobs", "Government Jobs"), 
            ("Entrepreneurship", "Entrepreneurship"), 
            ("Content Creation", "Content Creation"), 
            ("Gaming", "Gaming"), 
            ("Animation", "Animation"), 
            ("Music", "Music"), 
            ("Photography", "Photography"), 
            ("Sports", "Sports"), 
            ("Agriculture", "Agriculture"), 
            ("Environment", "Environment"), 
            ("Psychology", "Psychology"), 
            ("Robotics", "Robotics"), 
            ("Architecture", "Architecture"), 
            ("Civil Services", "Civil Services"), 
            ("Defence", "Defence"), 
            ("Aviation", "Aviation"), 
            ("UI/UX Design", "UI/UX Design"), 
            ("Film Making", "Film Making"), 
            ("Public Speaking", "Public Speaking"), 
            ("Politics", "Politics"), 
            ("Economics", "Economics"), 
            ("Biotechnology", "Biotechnology")
        ],
    )

    def validate_passions(
        self,
        field
    ):

        if not field.data:

            raise ValidationError(
                "Please select at least one passion."
            )

    skills = MultiCheckboxField(
        "Choose The Skills You Know",
        choices=[],
    )

    dream_job = StringField(
        "Dream Job",
        validators=[
            Optional(),
            Length(max=255)
        ]
    )

    submit = SubmitField(
        "Save Profile"
    )