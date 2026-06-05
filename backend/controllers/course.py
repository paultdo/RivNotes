from sqlalchemy import select
from sqlalchemy.orm import Session
from models.course import Course

def create_course(db: Session, data):
    course = Course(**data.model_dump())
    db.add(course)
    db.commit() # save to database
    db.refresh(course) # fill in id, created_at, updated_at, etc
    return course

def get_course(db: Session, course_id: int):
    course = db.get(Course, course_id)
    return course

# to implement later: add pagination
def get_course_list(db: Session):
    return db.scalars(select(Course)).all()

def update_course(db: Session, course_id: int, data):
    course = db.get(Course, course_id)
    if course is None:
        return None
    course.name = data.name if data.name is not None else course.name
    course.department = data.department if data.department is not None else course.department
    course.course_code = data.course_code if data.course_code is not None else course.course_code
    db.commit()
    db.refresh(course)
    return course

def delete_course(db: Session, course_id: int):
    course = db.get(Course, course_id)
    if course is not None:
        db.delete(course)
        db.commit()
        return True
    
    return False
        


