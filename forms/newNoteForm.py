from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class NoteAddingForm(FlaskForm):
    header = StringField('Название заметки', validators=[DataRequired()])
    text = TextAreaField('Текст заметки', validators=[DataRequired()])
    submit = SubmitField('Добавить заметку', validators=[DataRequired()])
