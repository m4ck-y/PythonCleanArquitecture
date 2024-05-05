from dataclasses import dataclass
from enum import Enum

class UserType(Enum):
    Medic=1
    Assistant=2
    person=3

@dataclass
class UserEntity:
    id:int
    username:str
    email:str
    type:UserType
    password:str