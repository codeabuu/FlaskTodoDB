from flask_wtf import FlaskForm as Form
from wtforms.fields import StringField, PasswordField
from wtforms.validators import InputRequired, EqualTo

class TaskForm(Form):
    label = StringField('label', validators = [InputRequired()])

class LoginForm(Form):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
class RegForm(Form):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired()])
