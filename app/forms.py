from flask_wtf import FlaskForm as Form
from wtforms.fields import StringField
from wtforms.validators import InputRequired

class TaskForm(Form):
	label = StringField('label', validators = [InputRequired()])
