#from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField ,PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo,Required


class PitchForm(FlaskForm):
    content = TextAreaField('INPUT PITCH')
    submit = SubmitField('submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
  


