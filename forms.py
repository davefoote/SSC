from flask.ext.wtf import Form
from wtforms import validators
from wtforms.fields import TextField, TextAreaField, SubmitField

class ContactForm(Form):
  name = TextField('Name',  [validators.Required("A name is required.")])
  subject = TextField('Subject', [validators.Required("A subject is required.")])
  email = TextField('Email',  [validators.Required("An email is required."), validators.Email("Your email is incorrectly formatted.")])
  message = TextAreaField('Message',  [validators.Required("A message is required.")])
  submit = SubmitField('Send')
