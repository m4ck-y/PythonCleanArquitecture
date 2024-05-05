from abc import ABC, abstractmethod
from domain.entity.base.person import personEntity

class PersonRepository(ABC):
    
    @abstractmethod
    def Create(self, person:personEntity):
        raise NotImplementedError
    
    @abstractmethod
    def Get(id:int):
        raise NotImplementedError
    
    @abstractmethod
    def List(self):
        raise NotImplementedError
    
    @abstractmethod
    def Update(self, user:personEntity):
        raise NotImplementedError
    
    @abstractmethod
    def Delete(id:int):
        raise NotImplementedError

