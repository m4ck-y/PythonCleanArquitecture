from domain.repository.person import personRepository
from domain.entity.base.person import personEntity
from typing import List, Dict
from .file_manager import *

class PersonRepositoryFile(personRepository):

    def __init__(self) -> None:
        super().__init__()
        self.nameFileDB = "data.json"
        self.n = 0
        self.data:Dict[int, personEntity] = read_json(self.nameFileDB)

    def Create(self, person:personEntity):
        self.n += self.n
        self.data[person.id] = person
        write_json(self.nameFileDB, self.data)

    def Get(self, id:int):
        self.data.get(id, personEntity())
    
    def List(self)->List[personEntity]:
        return list(self.data.values())
    
    def Update(self, person:personEntity):
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
    