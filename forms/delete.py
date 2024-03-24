from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField


class DeleteNote(FlaskForm):
    id = HiddenField()
    submit = SubmitField('Удалить')
