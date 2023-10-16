from flask.ext.wtf import Form
from wtforms.fields import StringField
from wtforms.validators import InputRequired

class TaskForm(Form):
	label = StringField('label', validators = [InputRequired()])
