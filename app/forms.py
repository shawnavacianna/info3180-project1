from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields import TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Email
from app import allowed_extensions

class SignUpForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField("Last Name", validators=[DataRequired()])
    gender = SelectField("Gender", choices=[("None", "Select Gender"), ("Male", "Male"), ("Female", "Female")], validators=[DataRequired()])
    email = StringField("Email", validators = [DataRequired(), Email()])
    location = StringField("Location", validators = [DataRequired()])
    biography = TextAreaField("Biography", validators = [DataRequired()])
    photo = FileField(validators=[FileRequired(), FileAllowed(allowed_extensions)])
