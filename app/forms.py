from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, InputRequired

class SignUpForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField()

class AddressForm(FlaskForm):
    address = StringField('Address', validators=[InputRequired()])
    apartment = StringField('Apartment, Suite, etc.', validators=[])
    city = StringField('City', validators=[InputRequired()])
    state= StringField('State', validators= [InputRequired()])
    country= StringField('Country', validators= [InputRequired()])
    zip = StringField('Zip', validators=[InputRequired()])
    submit =SubmitField()

class PhoneForm(FlaskForm):
    number= StringField('Phone Number', validators=[InputRequired()])
    provider= StringField('Provider', validators=[InputRequired()])
    provided_to = StringField("Provided To", validators=[])
    submit= SubmitField()

class ProvideForm(FlaskForm):
    provided_to= StringField("Provide TO", validators=[] )
    submit= SubmitField()