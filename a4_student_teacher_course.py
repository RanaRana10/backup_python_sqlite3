from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

db_location = "3_students_teacher_course.db"
engine = create_engine(f"sqlite+pysqlite:///{db_location}", echo= False)

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key= True)
    roll_no = Column(Integer)
    name = Column(String)
    phone_no = Column(String)
    email = Column(String)

    parent_id = Column(Integer, ForeignKey('parents.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))

    parent = relationship("Parent", back_populates= "student")
    course = relationship("Course", back_populates= "student")


    def __init__(self,
                 id: str = None,
                 roll_no: int = None,
                 name: str = "Not_Given",
                 phone_no: str = "Not_Given",
                 email: str = "Not_Given",
                 parent_id: int = None,
                 course_id: int = None
                 ):
        self.id = id
        self.roll_no = roll_no
        self.name = self.calculate_name(name)
        self.phone = "+91" + " " + str(phone_no)
        self.email = email.lower()

        self.parent_id = parent_id
        self.course_id = course_id

    def calculate_name(self, name: str) -> str:
        if name.lower() in ["hello", "rana", "razor"]:
            return "ADMIN"
        else:
            return name.upper()


class Parent(Base):
    __tablename__ = 'parents'

    id = Column(Integer, primary_key= True)
    name = Column(String)
    phone_no = Column(String)
    pin_code = Column(Integer)

    student = relationship("Student", back_populates= "parent")

    def __init__(self, id: int = None, name:str = "Not_Given",
                 phone_no:str = "Not_Given", pin_code:int = None):
        self.id = id
        self.name = name.upper()
        self.phone_no = "+91" + " " + str(phone_no)
        self.pin_code = pin_code


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key= True)
    name = Column(String)
    fee = Column(Integer)
    duration_months = Column(Integer)

    student = relationship("Student", back_populates= "course")

    def __init__(self, id:int = None, name:str = "Not_Given",
                 fee: int = None, duration_months: int = None):
        self.id = id 
        self.name = name.upper()
        self.fee = fee + 100 #100 is the extra charge of the payment for gst tax
        self.duration_months = duration_months


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


parents_data = [
    {'name': 'Michael Johnson', 'phone_no': 9998887777, 'pin_code': 112233},
    {'name': 'Emma Smith', 'phone_no': 1112223333, 'pin_code': 223344},
    {'name': 'David Lee', 'phone_no': 7777777777, 'pin_code': 334455},
    {'name': 'Sarah Wilson', 'phone_no': 8888888888, 'pin_code': 445566},
    {'name': 'John Davis', 'phone_no': 5555555555, 'pin_code': 556677}
]

# for data in parents_data:
#     parent = Parent(**data)
#     session.add(parent)

courses_data = [
    {'name': 'Mathematics', 'fee': 2000, 'duration_months': 6},
    {'name': 'Science', 'fee': 2500, 'duration_months': 8},
    {'name': 'English Literature', 'fee': 1800, 'duration_months': 5},
    {'name': 'History', 'fee': 2200, 'duration_months': 7},
    {'name': 'Computer Science', 'fee': 3000, 'duration_months': 9}
]

# for data in courses_data:
#     course = Course(**data)
#     session.add(course)

# Insert Students Data
students_data = [
    {'roll_no': 101, 'name': 'John Doe', 'phone_no': 1234567890, 'email': 'john@example.com', 'parent_id': 1, 'course_id': 1},
    {'roll_no': 102, 'name': 'Jane Smith', 'phone_no': 9876543210, 'email': 'jane@example.com', 'parent_id': 2, 'course_id': 2},
    {'roll_no': 103, 'name': 'Alice Johnson', 'phone_no': 5551234567, 'email': 'alice@example.com', 'parent_id': 1, 'course_id': 3},
    {'roll_no': 104, 'name': 'Michael Lee', 'phone_no': 7778889999, 'email': 'michael@example.com', 'parent_id': 3, 'course_id': 4},
    {'roll_no': 105, 'name': 'Sara Brown', 'phone_no': 2223334444, 'email': 'sara@example.com', 'parent_id': 4, 'course_id': 1},
    {'roll_no': 106, 'name': 'David Wilson', 'phone_no': 6667778888, 'email': 'david@example.com', 'parent_id': 2, 'course_id': 5},
    {'roll_no': 107, 'name': 'Emily Davis', 'phone_no': 4445556666, 'email': 'emily@example.com', 'parent_id': 3, 'course_id': 2},
    {'roll_no': 108, 'name': 'Ryan Johnson', 'phone_no': 9990001111, 'email': 'ryan@example.com', 'parent_id': 4, 'course_id': 3},
    {'roll_no': 109, 'name': 'Sophia Lee', 'phone_no': 1231231234, 'email': 'sophia@example.com', 'parent_id': 1, 'course_id': 4},
    {'roll_no': 110, 'name': 'Matthew Harris', 'phone_no': 9876543210, 'email': 'matthew@example.com', 'parent_id': 2, 'course_id': 5}
]

# for data in students_data:
#     student = Student(**data)
#     session.add(student)

# session.commit()
# session.close()



# students_query = session.query(Student).join(Parent).join(Course).filter(Student.name == "JOHN DOE").order_by(Student.id.desc()).limit(3).all()

# for student in students_query:
#     print(f"Student ID: {student.id}, Roll No: {student.roll_no}, Name: {student.name}, Phone: {student.phone_no}, Email: {student.email}")
#     print(f"Parent: {student.parent.name}, Phone: {student.parent.phone_no}, Pin Code: {student.parent.pin_code}")
#     print(f"Course: {student.course.name}, Fee: {student.course.fee}, Duration (months): {student.course.duration_months}")
#     print("="*50)

# session.close()

std_1 = Student(roll_no= 1, name = "pllkpythonkjfdfdsgfdgfhfghfgfdgsdfgsfdg")
session.add(std_1)
session.commit()











