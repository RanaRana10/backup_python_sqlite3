from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, select

db_location = "zzz_multiple_table.db"
engine = create_engine(f"sqlite:///{db_location}")

metadata = MetaData()

users_table = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('email', String)
)

orders_table = Table('orders', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer),
    Column('product', String),
    Column('quantity', Integer)
)
metadata.create_all(engine)

users_data = [
    {'name': 'Alice', 'email': 'alice@example.com'},
    {'name': 'Bob', 'email': 'bob@example.com'},
    {'name': 'Charlie', 'email': 'charlie@example.com'}]

orders_data = [
    {'user_id': 1, 'product': 'Laptop', 'quantity': 1},
    {'user_id': 2, 'product': 'Monitor', 'quantity': 2},
    {'user_id': 1, 'product': 'Keyboard', 'quantity': 1}]


with engine.connect() as connection:
    connection.execute(users_table.insert(), users_data)
    connection.execute(orders_table.insert(), orders_data)
    # connection.commit()


# with engine.connect() as connection:
#     stmt = select(users_table.c.id, users_table.c.name).where(users_table.c.id >= -92)
#     print(stmt)
#     result = connection.execute(stmt).fetchall()
#     print("Results:")
#     for row in result:
#         print(row)



# with engine.connect() as connection:
#     stmt = select(users_table.c.id, users_table.c.name, orders_table.c.product, orders_table.c.quantity)\
#         .select_from(users_table.join(orders_table, users_table.c.id == orders_table.c.user_id))
    
#     print(stmt)
#     result = connection.execute(stmt).fetchall()
#     print("Results:")
#     for row in result:
#         print(row)


with engine.connect() as connection:
    stmt = select(users_table.c.id, users_table.c.name, orders_table.c.product, orders_table.c.quantity).select_from(users_table.join(orders_table, users_table.c.id == orders_table.c.user_id))
    
    print(stmt)
    result = connection.execute(stmt).fetchall()
    print(result)






# with engine.connect() as connection:
#     users_result = connection.execute(users_table.select()).fetchall()
#     print("Users:")
#     for user in users_result:
#         print(user)

#     orders_result = connection.execute(orders_table.select()).fetchall()
#     print("\nOrders:")
#     for order in orders_result:
#         print(order)

#     combined_result = connection.execute(
#         users_table.join(orders_table, users_table.c.id == orders_table.c.user_id)
#                    .select()
#     ).fetchall()

#     print("\nCombined Results (Selected Columns from Users and Orders):")
#     for row in combined_result:
#         print(row)








































