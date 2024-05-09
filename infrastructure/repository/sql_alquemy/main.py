from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:12345678@localhost:3306/db_name", echo=True)
meta = MetaData()
conn = engine.connect()

from .person import person #migrations
#selectall
conn.execute(person.select()).fetchall()
#insert
result = conn.execute(person.insert().values({"name":"", "pass":""}))
"return"
conn.execute(person.select().where(person.c.id == result.lastrowid)).first()

def insert(username:str, email:str):
    query = person.insert().values(username=username,email=email)
    conn.execute(query)