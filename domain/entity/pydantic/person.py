from pydantic import BaseModel
from datetime import datetime

class PersonEntity(BaseModel):
    id:int=0
    name:str=0
    last_name:str=0
    second_last_name:str=""
    photo_url:str=""
    email:str=""
    id_user:int=0
    birthdate:datetime