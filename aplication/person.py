from domain.repository.person import personRepository
from domain.entity.base.person import personEntity

class Person:

    def __init__(self, repository:personRepository) -> None:
        self.repository = repository

    def add(self, person:  personEntity):
        self.repository.add(person)
