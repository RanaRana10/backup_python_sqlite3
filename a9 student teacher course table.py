from sqlalchemy import create_engine, MetaData, ForeignKey, select
from sqlalchemy import Table, Column, Integer, String

db_location = "students_parents_course.db"
engine = create_engine(f"sqlite+pysqlite:///{db_location}")

metadata = MetaData()

students_table = Table(
    'students', metadata,
    Column('id', Integer, primary_key=True),
    Column('rollno', Integer),
    Column('name', String),
    Column('phone', Integer),
    Column('email', String),
    Column('parent_id', Integer, ForeignKey('parents.id')),
    Column('course_id', Integer, ForeignKey('courses.id')),
)

parents_table = Table(
    'parents', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('phone', Integer),
    Column('pin_code', Integer),
)

courses_table = Table(
    'courses', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fee', Integer),
    Column('duration_months', Integer),
)

metadata.create_all(engine)

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

def insert_data(): 
    with engine.connect() as connection:
        result_1 = connection.execute(students_table.insert().values(students_data))
        result_2 = connection.execute(parents_table.insert().values(parents_data))
        result_3 = connection.execute(courses_table.insert().values(courses_data))
        connection.commit()

insert_data #once data is inserted then remove the () brackets so that the problem of unique id not show error


with engine.connect() as connection:
    stmt = select(students_table.c.id, students_table.c.name, parents_table.c.name, courses_table.c.name)\
        .select_from(students_table\
                     .join(parents_table, students_table.c.parent_id == parents_table.c.id)\
                     .join(courses_table, students_table.c.course_id == courses_table.c.id))
    print(stmt)
    result = connection.execute(stmt).fetchall()
    for _ in result:
        print("id is:", _[0], "& Student Name:", _[1], "& Father:", _[2], "& Subject:", _[3])




