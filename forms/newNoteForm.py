from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class NoteAddingForm(FlaskForm):
    header = StringField('Название заметки', validators=[DataRequired()])
    text = TextAreaField('Текст заметки', validators=[DataRequired()])
    note_type = SelectField('Тип заметки', choices=['default', 'news'])
    submit = SubmitField('Добавить заметку')
