from fastapi import HTTPException
from .config_sqlite import Base, engine, Session
from sqlalchemy import Column, Integer, String

from typing import Optional
from sqlalchemy.orm import Mapped, relationship
class UserTable(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    type = Column(Integer)

    person:Mapped[Optional["TablePerson"]] = relationship("TablePerson", back_populates="user")

from sqlalchemy.orm import mapped_column
class UserTable2(Base):
    __tablename__ = "users2"

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username:Mapped[str] = mapped_column(String(100))
    email:Mapped[str]
    password:Mapped[str]
    type:Mapped[int]



Base.metadata.create_all(bind=engine)

from domain.repository.user import UserRepository
from domain.entity.base.user import UserEntity as E
from typing import List

class UserRepositorySQLAlcchemy(UserRepository):
    
    def Create(self, value:E):
        with Session() as db:
            newUser = UserTable(**value.model_dump())
            #FAZT: db.execute(FruitTable.insert().values(value))
            db.add(newUser)
            db.commit()
    
    def Get(self, id:int)->E|None:
       with Session() as db:
           #FAZT: db.execute(FruitTable.select().where(FruitTable.id == id))
           result = db.query(UserTable).filter(UserTable.id == id).first()
           return result
    
    def List(self)->List[E]:
        with Session() as db:
            result = db.query(UserTable).all()
            #FAZT: db.execute(FruitTable.select()).fetchall()
            return result
    
    def Update(self, value:E):
        with Session() as db:
            result = db.query(UserTable).filter(UserTable.id == value.id).first()
            if result is None:
                raise HTTPException(404, "Not FOund")
            for k, v in value.model_dump().items():
                setattr(result, k, v)
            db.commit()
            db.refresh(result)
            #FAZT: 
            return result
    
    def Delete(self, id:int):
        with Session() as db:
            result = db.query(UserTable).filter(UserTable.id == id).first()
            db.delete(result)
            #FAZT: db.execute(FruitTable.delete().where(FruitTable.id==id))
            db.commit()
            return result

