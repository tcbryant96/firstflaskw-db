from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class registerform(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone_num= StringField('Phone Number', validators=[DataRequired()])
    address= StringField('Address', validators=[DataRequired()])
    submit= SubmitField()