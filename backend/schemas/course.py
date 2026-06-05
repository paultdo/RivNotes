from datetime import datetime
from pydantic import BaseModel, ConfigDict

class CourseCreate(BaseModel):
    name: str
    department: str
    course_code: str

class CourseUpdate(BaseModel):
    name: str | None = None
    department: str | None = None
    course_code: str | None = None

class CourseRead(BaseModel):
    id: int
    name: str
    department: str
    course_code: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class CourseDelete(BaseModel):
    id: int