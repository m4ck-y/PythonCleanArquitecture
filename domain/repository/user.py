from abc import ABC, abstractmethod
from domain.entity.base.user import UserEntity
from typing import List

class UserRepository(ABC):
    
    @abstractmethod
    def Create(self, value:UserEntity):
        raise NotImplementedError
    
    @abstractmethod
    def Get(self, id:int)->UserEntity|None:
        raise NotImplementedError
    
    @abstractmethod
    def List(self)->List[UserEntity]:
        raise NotImplementedError
    
    @abstractmethod
    def Update(self, person:UserEntity):
        raise NotImplementedError
    
    @abstractmethod
    def Delete(self, id:int):
        raise NotImplementedError

