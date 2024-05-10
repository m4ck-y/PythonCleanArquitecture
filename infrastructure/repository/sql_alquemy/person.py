from .main import db, Base, session

from sqlalchemy.orm import Mapped, mapped_column, relationship

class Person(Base):
    __tablename__  = "person"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    name:Mapped[str]
    last_name:Mapped[str]
    second_last_name:Mapped[str]
    photo_url:Mapped[str]
    #id_user:Mapped[int]
    user:Mapped["User"] = relationship("User", back_populates="")

    def __repr__(self) -> str:
        return f"<Person(id={self.id},name={self.name},last_name={self.last_name},second_last_name={self.second_last_name},photo_url={self.photo_url})>"

class User(Base):
    __tablename__ = "user"

    id:Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    name:Mapped[str]

def main():
    Base.metadata.create_all(db)
    person = Person(id=2,name="de")
    person.photo_url = "ff"

    with session() as sess:
        sess.add(person)
        sess.commit()
        print(sess.query(Person).all())




