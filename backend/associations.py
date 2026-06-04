from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import mapped_column
from database import Base

user_course_association = Table(
    "user_course",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True),
)

user_note_association = Table(
    "user_note",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("note_id", ForeignKey("notes.id"), primary_key=True),
)