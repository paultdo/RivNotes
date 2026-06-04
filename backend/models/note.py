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
from associations import user_note_association

class Note(Base):
    __tablename__ = "notes"
    id: Mapped[int] = mapped_column(primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    name: Mapped[str] = mapped_column(String)
    filepath: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), 
        onupdate=func.now()
    )

    users: Mapped[List["User"]] = relationship(
        secondary=user_note_association, 
        back_populates="notes"
    )

    def __repr__(self) -> str:
        return f"Note(id={self.id!r}), course_id={self.course_id!r}, name={self.name!r}, filepath={self.filepath}"



