from .config_sqlite import Base, engine, Session

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from typing import Optional

from .user import UserTable

from datetime import datetime

class TablePerson(Base):
    __tablename__  = "person"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    name:Mapped[str]
    last_name:Mapped[str]
    second_last_name:Mapped[str]
    photo_url:Mapped[str]
    email:Mapped[str]
    birthdate:Mapped[datetime]
    id_user:Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))
    user:Mapped[Optional[UserTable]] = relationship("UserTable", back_populates="person")

    def __repr__(self) -> str:
        return f"<Person(id={self.id},name={self.name},last_name={self.last_name},second_last_name={self.second_last_name},photo_url={self.photo_url})>"

Base.metadata.create_all(bind=engine)

from domain.repository.person import PersonRepository
from domain.entity.base.person import PersonEntity as E
from typing import List

class PersonRepositorySQLAlcchemy(PersonRepository):
    
    def Create(self, value:E):
        with Session() as db:
            newUser = TablePerson(**value.model_dump())
            #FAZT: db.execute(FruitTable.insert().values(value))
            db.add(newUser)
            db.commit()
    
    def Get(self, id:int)->E|None:
       with Session() as db:
           #FAZT: db.execute(FruitTable.select().where(FruitTable.id == id))
           result = db.query(TablePerson).filter(TablePerson.id == id).first()
           return result
    
    def List(self)->List[E]:
        with Session() as db:
            result = db.query(TablePerson).all()
            #FAZT: db.execute(FruitTable.select()).fetchall()
            return result
    
    def Update(self, value:E):
        with Session() as db:
            result = db.query(TablePerson).filter(TablePerson.id == value.id).first()
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
            result = db.query(TablePerson).filter(TablePerson.id == id).first()
            db.delete(result)
            #FAZT: db.execute(FruitTable.delete().where(FruitTable.id==id))
            db.commit()
            return result
