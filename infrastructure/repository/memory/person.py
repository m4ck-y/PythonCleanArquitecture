from domain.repository.person import PersonRepository
from domain.entity.base.person import PersonEntity
from typing import List, Dict

class PersonRepositoryMemory(PersonRepository):
    def __init__(self):
        self.n = 0
        self.data:Dict[int, PersonEntity] = {}

    def Get(self, id:int)->PersonEntity:
        self.data.get(id, PersonEntity())

    def List(self)->List[PersonEntity]:
        return list(self.data.values())

    def Create(self, person:PersonEntity):
        self.n += self.n
        self.data[person.id] = person

    def Update(self, person:PersonEntity)-> bool:
        finded = self.data.get(person.id, None)
        if finded == None:
            return False
        
        finded.age = person.age
        finded.name = person.name
        return True
        

    def Delete(self, id:int) -> bool:
        finded = self.data.get(id, None)
        if finded == None:
            self.data

        del self.data[id]
        return True