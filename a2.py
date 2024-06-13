from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker


location_db = "1_practise_db.db"
engine = create_engine(f"sqlite+pysqlite:///{location_db}")

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person_information'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)

    def __init__(self,
                 id: int = None,
                 name: str= "NoName",
                 age: int = 000,
                 email: str = "No_Email"):
        
        self.id = id
        self.name = name.upper()
        self.age = age
        self.email = email.lower()


Base.metadata.create_all(engine)
Session = sessionmaker(bind= engine)
session = Session()

person1 = Person(name= "Manik Rana", age= 33, email = "manik@mail.com")
person2 = Person(name = "Ratan")

session.add(person1)
session.add(person2)
session.commit()



# all_users = session.query(Person).all()
# for _ in all_users:
#     print(_.name, _.age, _.email)

