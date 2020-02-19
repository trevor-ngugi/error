#from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField ,PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class PitchForm(FlaskForm):
    content = TextAreaField('INPUT PITCH')
    submit = SubmitField('SUBMIT')

class CommentForm(FlaskForm):
    opinion = TextAreaField('WRITE COMMENT')
    submit = SubmitField('SUBMIT')

class CategoryForm(FlaskForm):
    name =  StringField('Category Name', validators=[Required()])
    submit = SubmitField('Create')

class RegisterForm(FlaskForm):
  username= StringField('Username', validators=[DataRequired(), Length(min=2, max=10) ])
  email= StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
  submit=SubmitField('Sign Up')

class LoginForm(FlaskForm):
  email= StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit=SubmitField('Sign In')
  


