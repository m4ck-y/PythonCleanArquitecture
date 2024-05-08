from domain.repository.user import UserRepository
from domain.entity.base.user import UserEntity
from typing import List, Dict

class UserRepositoryMemory(UserRepository):
    def __init__(self):
        self.n = 0
        self.data:Dict[int, UserEntity] = {}

    def Get(self, id:int)->UserEntity:
        return self.data.get(id, UserEntity())

    def List(self)->List[UserEntity]:
        return list(self.data.values())

    def Create(self, value:UserEntity):
        self.n += self.n
        self.data[value.id] = value

    def Update(self, value:UserEntity)-> bool:
        found = self.data.get(value.id, None)
        if found == None:
            return False
        
        #TODO: Update complete object
        found.username = value.username
        return True
        

    def Delete(self, id:int) -> bool:
        found = self.data.get(id, None)
        if found == None:
            return False

        del self.data[id]
        return True