from sqlalchemy import create_engine, URL
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

""" url_object = URL.create(
    drivername="sqlite",
    username="root",
    password="password",  # plain (unescaped) text
    host="localhost",
    database="laramedic",
) """

url_object = "sqlite:///file.db"


engine = create_engine(url_object, echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()



#migrtions base
from sqlalchemy import Column, Integer, String, Float

class FruitTable(Base):
    __tablename__ = "fruits"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    sugar = Column(Float)

#session engine Base, migratios.Fruit SERVICE
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

class Fruit(BaseModel):
    id:int
    name:str
    sugar:float

Base.metadata.create_all(bind=engine)

#create
app = FastAPI()
from typing import List
@app.get("/fruit/")
def List()->List[Fruit]:
    db = Session()
    result = db.query(FruitTable).all()
    return result

@app.get("/fruit/{id}")
def List(id:int)->Fruit:
    db = Session()
    result = db.query(FruitTable).filter(FruitTable.id == id).first()
    return result

@app.post("/fluit")
def Create(value:Fruit):

    db = Session()
    new_fruit = FruitTable(**value.model_dump())
    db.add(new_fruit)
    db.commit()
    return value

@app.update("/fluit")
def Update(id:int, value:Fruit):
    with Session() as db:
        result = db.query(FruitTable).filter(FruitTable.id == value.id).first()
        if result is None:
            raise HTTPException(404, "Not FOund")
        for k, v in value.model_dump().items():
            setattr(result, k, v)
        db.commit()
        db.refresh(result)
        return result

@app.delete("/fluit")
def Delete(id:int):
    db = Session()
    result = db.query(FruitTable).filter(FruitTable.id == id).first()
    db.delete(result)
    db.commit()
    return result
#


import uvicorn
if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0")