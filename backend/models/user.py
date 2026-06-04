from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
from associations import user_course_association, user_note_association

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    password: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), 
        onupdate=func.now()
    )

    courses: Mapped[List["Course"]] = relationship(
        secondary=user_course_association, 
        back_populates="users"
    )

    notes: Mapped[List["Note"]] = relationship(
        secondary=user_note_association, 
        back_populates="users"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}), email={self.email!r}, username={self.username!r}"



