from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

location_db = "practise_db.db"
engine = create_engine(f"sqlite+pysqlite:///{location_db}")

metadata = MetaData()

users_table = Table('users_7', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(4)),
    Column('age', Integer),
    Column('address', String, default= "India"),
    Column('third_party', String, default= None)
)
metadata.create_all(engine)

data_to_insert = [
    {'name': 'Bob', 'age': 25},
    {'name': 'Alice', 'age': 30},
    {'name': 'Manoo', 'age': 28}
]

try:
    with engine.connect() as connection:
        for data in data_to_insert:
            # Truncate name if it exceeds 4 characters
            data['name'] = data['name'][:4]
            result = connection.execute(users_table.insert().values(data))
        # inserted_data = connection.execute(users_table.select().where(users_table.c.name == "Bob")).fetchall()

        search_data = connection.execute(users_table.select().where(users_table.c.age > 29)).fetchall()

        print(search_data)
        connection.commit()

        print("Data Inserted Successfully!")

except Exception as e:
    print(f"\033[90m{e} \033[0m")











