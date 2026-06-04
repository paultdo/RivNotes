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
from associations import user_course_association

class Course(Base):
    __tablename__ = "courses"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    department: Mapped[str] = mapped_column(String)
    course_code: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), 
        onupdate=func.now()
    )

    users: Mapped[List["User"]] = relationship(
        secondary=user_course_association, 
        back_populates="courses"
    )

    def __repr__(self) -> str:
        return f"Course(id={self.id!r}), name={self.name!r}, department={self.department!r}, course_code={self.course_code}"



