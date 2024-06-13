from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

location_db = "practise_db.db"
engine = create_engine(f"sqlite+pysqlite:///{location_db}")

metadata = MetaData()

users_table = Table('users_2', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, default= "None"),
    Column('age', Integer, default= 0),
    Column('email', String, default=None),  
    Column('location', String, default=None)  
)

metadata.create_all(engine)

data_to_insert = [{'name':"Rana", 'age':34}]

data_to_insert = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {}
]
try:
    with engine.connect() as connection:
        result = connection.execute(users_table.insert().values(data_to_insert))
        connection.commit()
        print("Data Inserted Successfully!")
        last_inserted_id = int(result.lastrowid)

        inserted_data = connection.execute(users_table.select().where(users_table.c.id == last_inserted_id-1-1)).fetchone()
        print("Inserted Data:")
        print("ID:", inserted_data[0])
        print("Name:", inserted_data[1])
        print("Age:", inserted_data[2])
        print("Email:", inserted_data[3])
        print("Location:", inserted_data[4])

except Exception as e:
    print(f"\033[90m{e} \033[0m")

