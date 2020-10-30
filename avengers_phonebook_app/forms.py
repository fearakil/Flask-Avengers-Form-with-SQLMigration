from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired,EqualTo, Email

# DataRequired == Making sure the field is filled in
# EqualTo == Making sure the field(s) are the same (I.E Password and Confirm Password)
# Email == Making sure the field has  a proper email given to it 

class UserInfoForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    phone = StringField('Phone', validators = [DataRequired()])
    email = StringField('Email',validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = StringField('Password', validators = [DataRequired()])
    submit = SubmitField()

class ContactPost(FlaskForm):
    role = StringField('Role', validators = [DataRequired()])
    phone_number = StringField('Phone Number', validators = [DataRequired()])
    submit = SubmitField()