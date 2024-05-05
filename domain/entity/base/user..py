from enum import Enum

class UserType(Enum):
    Medic=1
    Assistant=2
    person=3

class UserEntity:

    def __init__(self,
                id:int,
                username:str,
                email:str,
                type:UserType,
                password:str) -> None:
        
        self.id = id
        self.username = username
        self.email = email
        self.type = type
        self.password = password