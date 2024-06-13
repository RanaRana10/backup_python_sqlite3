from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select, and_, func

location_db = "practise_db.db"
engine = create_engine(f"sqlite+pysqlite:///{location_db}")

metadata = MetaData()

users_table = Table('users_7', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(4)),
    Column('age', Integer),
    Column('address', String, default="India"),
    Column('third_party', String, default=None)
)
metadata.create_all(engine)

data_to_insert = [
    {'name': 'Bob', 'age': 25},
    {'name': 'Alice', 'age': 30},
    {'name': 'Manoo', 'age': 28}
]

# try:
#     with engine.connect() as connection:
#         result = connection.execute(users_table.insert().values(data_to_insert))
#         connection.commit()

# except Exception as e:
#     print(f"\033[90m{e} \033[0m")


# with engine.connect() as connection:
#     search_data = connection.execute(users_table.select().where(and_(users_table.c.age > 9, users_table.c.name == 'Bob'))).fetchall()
#     print(search_data)

with engine.connect() as connection:
    search_data = connection.execute(users_table.select().where(and_(users_table.columns.age > 9, users_table.columns.name == 'Bob'))).fetchone()
    print(search_data)






