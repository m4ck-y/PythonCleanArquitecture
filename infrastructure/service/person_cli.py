from aplication.person import Person
from infrastructure.repository.person_repository_memory import PersonRepositoryMemory
from domain.port.person_repository import PersonRepository
from domain.person import PersonEntity
from typing import List

class PersonCLI:
    def __init__(self) -> None:
        
        repository:PersonRepository = PersonRepositoryMemory()
        self.aplication = Person(repository)
        input("dame el valor")

    def add(self, person:PersonEntity):
        self.aplication.add(person)

    def list()->List[PersonEntity]:
        pass

