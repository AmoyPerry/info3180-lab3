# In forms.py create a Python class called ContactForm to represent
# your form using the various field types and validators available to you
# in Flask-WTF. Your form should have a text field for name, email,
# subject and a text area for a message.



from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
from wtforms.validators import InputRequired, Email


class ContactForm (FlaskForm):
 name = StringField('Name', validators=[InputRequired()])
 email = StringField('Email', validators=[InputRequired(), Email()])
 subject = StringField('Subject', validators=[InputRequired()])
 message = TextAreaField('Message', validators=[InputRequired()])