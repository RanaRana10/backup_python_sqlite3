from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

db_location = "sqlite:///users.db"
engine = create_engine(db_location, echo=0)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)

    def __init__(self, id = None, username: str = "Default Username", email: str = "default@example.com"):
        self.id = id
        self.username = username
        self.email = email

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()




user1 = User(username='john_doe', email='john@example.com')
user2 = User(username='jane_smith', email='jane@example.com', id = 99)
user3 = User(username='alice_wonder', email='alice@example.com')

# session.add(user1)
# session.add(user2)
# session.add(user3)
users_to_insert = [
    User(username='emma_smith', email='emma@example.com'),
    User(username='michael_jones', email='michael@example.com'),
    User(username='julia_roberts', email='julia@example.com'),
    User(username='robert_downey', email='robert@example.com'),
    # Add more User objects here as needed
]
session.bulk_save_objects(users_to_insert)


user1 = User(username='john_doe', email='john@example.com')
user2 = User(username='jane_smith', email='jane@example.com', id = 99)

session.add(user1)



# session.commit()
session.close()


all_users = session.query(User).all()
for user in all_users:
    # print(f"User ID: {user.id}, Username: {user.username}, Email: {user.email}")
    pass

# user_id_3 = session.query(User).filter(User.id == 3).first()
# if user_id_3:
#     print(f"User ID: {user_id_3.id}, Username: {user_id_3.username}, Email: {user_id_3.email}")
# else:
#     print("User with ID 3 not found.")


user_ids_to_fetch = [1,2]
users_in_list = session.query(User).filter(User.id.in_(user_ids_to_fetch)).all()
for users_in_list_i in users_in_list:
    # print(users_in_list_i.username)
    pass

users_with_name_like = session.query(User).filter(User.email.like('%com')).all()
for _ in users_with_name_like:
    print(_.username)
