from domain.repository.person import PersonRepository
from domain.entity.base.person import PersonEntity
from typing import List, Dict

class PersonRepositoryMemory(PersonRepository):
    def __init__(self):
        self.n = 0
        self.data:Dict[int, PersonEntity] = {}

    def Get(self, id:int)->PersonEntity:
        return self.data.get(id, PersonEntity())

    def List(self)->List[PersonEntity]:
        return list(self.data.values())

    def Create(self, person:PersonEntity):
        self.n += self.n
        self.data[person.id] = person

    def Update(self, person:PersonEntity)-> bool:
        found = self.data.get(person.id, None)
        if found == None:
            return False
        
        #TODO: Update complete object
        found.name = person.name
        return True
        

    def Delete(self, id:int) -> bool:
        found = self.data.get(id, None)
        if found == None:
            return False

        del self.data[id]
        return True