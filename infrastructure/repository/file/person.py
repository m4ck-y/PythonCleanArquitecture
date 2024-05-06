from domain.repository.person import PersonRepository
from domain.entity.base.person import PersonEntity
from typing import List, Dict
from .file_manager import *

class PersonRepositoryFile(PersonRepository):

    def __init__(self) -> None:
        super().__init__()
        self.nameFileDB = "data.json"
        self.n = 0
        self.data:Dict[int, PersonEntity] = read_json(self.nameFileDB)

    def Create(self, person:PersonEntity):
        self.n += self.n
        self.data[person.id] = person
        write_json(self.nameFileDB, self.data)

    def Get(self, id:int):
        self.data.get(id, PersonEntity())
    
    def List(self)->List[PersonEntity]:
        return list(self.data.values())
    
    def Update(self, person:PersonEntity):
        finded = self.data.get(person.id, None)
        if finded == None:
            return False
        
        self.data[person.id]=person
        write_json(self.nameFileDB, self.data)
        return True

    def Delete(self, id:int):
        finded = self.data.get(id, None)
        if finded == None:
            return False

        del self.data[id]
        write_json(self.nameFileDB, self.data)
        return True
    