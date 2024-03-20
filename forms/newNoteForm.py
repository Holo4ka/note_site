from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class NoteAddingForm(FlaskForm):
    header = StringField('Название заметки', validators=[DataRequired()])
    text = TextAreaField('Заметка', validators=[DataRequired()])
    add = SubmitField('Добавитьб заметку', validators=[DataRequired()])
