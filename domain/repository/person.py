from abc import ABC, abstractmethod
from domain.entity.base.person import PersonEntity
from typing import List

class PersonRepository(ABC):
    
    @abstractmethod
    def Create(self, person:PersonEntity):
        raise NotImplementedError
    
    @abstractmethod
    def Get(self, id:int)->PersonEntity|None:
        raise NotImplementedError
    
    @abstractmethod
    def List(self)->List[PersonEntity]:
        raise NotImplementedError
    
    @abstractmethod
    def Update(self, person:PersonEntity):
        raise NotImplementedError
    
    @abstractmethod
    def Delete(self, id:int):
        raise NotImplementedError

