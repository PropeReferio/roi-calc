from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class AddForm(FlaskForm):
    num1 = StringField("First Number", validators=[DataRequired()])
    num2 = StringField("Second Number", validators=[DataRequired()])
    submit = SubmitField("Submit")