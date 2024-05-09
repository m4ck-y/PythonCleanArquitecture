from pydantic import BaseModel
from enum import Enum
from typing import Optional

class UserType(Enum):
    Medic=1
    Assistant=2
    person=3

class UserEntity(BaseModel):
    id: int
    username: str
    email: str
    type: Optional[UserType] = 0

class UserDbEntity(UserEntity):
    password: str