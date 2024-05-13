from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

""" url_object = URL.create(
    drivername="sqlite",
    username="root",
    password="password",  # plain (unescaped) text
    host="localhost",
    database="laramedic",
) """

db_URL = "sqlite:///file_up.db"

engine = create_engine(db_URL, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()