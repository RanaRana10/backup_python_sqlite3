'''
This is a normal code where i checked on how to work
with multiple database
'''


from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

db_location = "a 10 students_parents_course_orm.db"
engine = create_engine(f"sqlite+pysqlite:///{db_location}")

Base = declarative_base()

class Parent(Base):
    __tablename__ = 'parents'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(Integer)
    pin_code = Column(Integer)

    students = relationship("Student", back_populates="parent")

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fee = Column(Integer)
    duration_months = Column(Integer)

    students = relationship("Student", back_populates="course")

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    rollno = Column(Integer)
    name = Column(String)
    phone = Column(Integer)
    email = Column(String)
    parent_id = Column(Integer, ForeignKey('parents.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))

    parent = relationship("Parent", back_populates="students")
    course = relationship("Course", back_populates="students")

Base.metadata.create_all(engine)



from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

students_data = [
    {'rollno': 101, 'name': 'John Doe', 'phone': 1234567890, 'email': 'john@example.com', 'parent_id': 1, 'course_id': 1},
    {'rollno': 102, 'name': 'Jane Smith', 'phone': 9876543210, 'email': 'jane@example.com', 'parent_id': 2, 'course_id': 2},
    {'rollno': 103, 'name': 'Alice Johnson', 'phone': 5551234567, 'email': 'alice@example.com', 'parent_id': 1, 'course_id': 3},
    {'rollno': 104, 'name': 'Michael Lee', 'phone': 7778889999, 'email': 'michael@example.com', 'parent_id': 3, 'course_id': 4},
    {'rollno': 105, 'name': 'Sara Brown', 'phone': 2223334444, 'email': 'sara@example.com', 'parent_id': 4, 'course_id': 1},
    {'rollno': 106, 'name': 'David Wilson', 'phone': 6667778888, 'email': 'david@example.com', 'parent_id': 2, 'course_id': 5},
    {'rollno': 107, 'name': 'Emily Davis', 'phone': 4445556666, 'email': 'emily@example.com', 'parent_id': 3, 'course_id': 2},
    {'rollno': 108, 'name': 'Ryan Johnson', 'phone': 9990001111, 'email': 'ryan@example.com', 'parent_id': 4, 'course_id': 3},
    {'rollno': 109, 'name': 'Sophia Lee', 'phone': 1231231234, 'email': 'sophia@example.com', 'parent_id': 1, 'course_id': 4},
    {'rollno': 110, 'name': 'Matthew Harris', 'phone': 9876543210, 'email': 'matthew@example.com', 'parent_id': 2, 'course_id': 5}
]

parents_data = [
    {'id': 1, 'name': 'Michael Johnson', 'phone': 9998887777, 'pin_code': 112233},
    {'id': 2, 'name': 'Emma Smith', 'phone': 1112223333, 'pin_code': 223344},
    {'id': 3, 'name': 'David Lee', 'phone': 7777777777, 'pin_code': 334455},
    {'id': 4, 'name': 'Sarah Wilson', 'phone': 8888888888, 'pin_code': 445566},
    {'id': 5, 'name': 'John Davis', 'phone': 5555555555, 'pin_code': 556677}
]

courses_data = [
    {'id': 1, 'name': 'Mathematics', 'fee': 2000, 'duration_months': 6},
    {'id': 2, 'name': 'Science', 'fee': 2500, 'duration_months': 8},
    {'id': 3, 'name': 'English Literature', 'fee': 1800, 'duration_months': 5},
    {'id': 4, 'name': 'History', 'fee': 2200, 'duration_months': 7},
    {'id': 5, 'name': 'Computer Science', 'fee': 3000, 'duration_months': 9}
]

for data in parents_data:
    parent = Parent(**data)
    session.add(parent)

for data in courses_data:
    course = Course(**data)
    session.add(course)

for data in students_data:
    student = Student(**data)
    session.add(student)

session.commit()


students = session.query(Student).\
    join(Parent, Student.parent_id == Parent.id).\
    join(Course, Student.course_id == Course.id).\
    all()

for student in students:
    print("id is:", student.id, "& Student Name:", student.name, "& Father:", student.parent.name, "& Subject:", student.course.name)

