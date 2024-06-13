from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

db_location = "2_books_data.db"
engine = create_engine(f"sqlite+pysqlite:///{db_location}", echo=0)

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))

    author = relationship("Author", back_populates="books")
    publisher = relationship("Publisher", back_populates= "books")

    def __init__(self, title="No Title", author=None, publisher=None):
        self.title = title
        self.author = author
        self.publisher = publisher


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key= True)
    name = Column(String)

    books = relationship("Book", back_populates= "author")

    def __init__(self, name: str = "No Name"):
        self.name = name





class Publisher(Base):
    __tablename__ = 'publishers'

    id = Column(Integer, primary_key= True)
    name = Column(String)

    books = relationship("Book", back_populates= "publisher")

    def __init__(self, name: str = "No Name"):
        self.name = name






Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()



# Create authors
author1 = Author(name="J.K. Rowling")
author2 = Author(name="George Orwell")

# Create publishers
publisher1 = Publisher(name="Penguin Books")
publisher2 = Publisher(name="Bloomsbury Publishing")

book1 = Book(title="Harry Potter and the Philosopher's Stone", author=author1, publisher=publisher2)
book2 = Book(title="1984", author=author2, publisher=publisher1)

session.add_all([author1, author2, publisher1, publisher2, book1, book2])

session.commit()

