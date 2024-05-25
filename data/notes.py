import sqlalchemy
from sqlalchemy import orm
import datetime
from .db_session import SqlAlchemyBase


class Note(SqlAlchemyBase):
    __tablename__ = "notes"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    text = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    header = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    note_type = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    creation_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    was_changed = sqlalchemy.Column(sqlalchemy.BOOLEAN, default=False, nullable=False)
    left = sqlalchemy.Column(sqlalchemy.Double)
    top = sqlalchemy.Column(sqlalchemy.Double)

    user = orm.relationship('User')
