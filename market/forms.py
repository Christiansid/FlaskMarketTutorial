from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User
class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check): #FlaskForm vill check for all functions that start with validate_ then check
        #afterward if there is a field that follows. In our case username exists, username==username; True
        user = User.query.filter_by(username=username_to_check.data).first()

        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email = User.query.filter_by(email_address = email_address_to_check.data).first()

        if email:
            raise ValidationError("Email Address already exists! Please try a different email address")

    username = StringField(label = 'User Name:', validators = [Length(min = 2, max = 30), DataRequired()] )
    email_address = StringField(label = 'Email Adress:', validators = [Email(), DataRequired()])
    password1 = PasswordField(label = 'Password:', validators = [Length(min = 6), DataRequired()])
    password2 = PasswordField(label = 'Confirm Password:', validators = [EqualTo('password1'), DataRequired()]) #Verifies that passwords are the same
    submit = SubmitField(label = 'Create Account')


