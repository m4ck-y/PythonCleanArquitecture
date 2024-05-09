from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from .main import engine, meta

person = Table("person", meta, Column("id", Integer, primary_key=True),
               Column("email", String(255)))

meta.create_all(engine)



