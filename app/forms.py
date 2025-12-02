from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CertificateForm(FlaskForm):
    student_name = StringField('Student Name', validators=[DataRequired()])
    course = StringField('Course Name', validators=[DataRequired()])
    submit = SubmitField('Issue Certificate')