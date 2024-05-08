from domain.repository.person import PersonRepository
from domain.entity.base.person import PersonEntity

class PersonApplication:

    def __init__(self, repository:PersonRepository) -> None:
        self.repository = repository

    def Create(self, person:  PersonEntity):
        return self.repository.Create(person)

    def Get(self, id:int):
        return self.repository.Get(id)

    def List(self):
        return self.repository.List()
    
    def Update(self, person:PersonEntity):
        return self.repository.Update(person)

    def Delete(self, id):
        return self.repository.Delete(id)