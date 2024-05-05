#from domain.entity.base.person import personEntity
from domain.entity.pydantic.person import personEntity
from infrastructure.repository.file.person import personRepository

class personServiceConsole:

    repository:personRepository

    def __init__(self, repository:personRepository) -> None:
        self.repository = repository

    def Add(self):
        import datetime
        person = personEntity(birthdate= datetime.datetime.now())
        
        person.id = 1
        person.name = input("Name:")
        person.last_name = input("Last Name:")
        person.second_last_name = input("Second Last Name:")
        person.email = input("email:")
        person.photo_url = input("url photo:")

        self.repository.Create(person)

        print("Created")


    def List(self):
        data = self.repository.List()

        print("Data:", data)