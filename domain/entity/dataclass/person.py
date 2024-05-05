from dataclasses import dataclass

@dataclass
class PersonEntity:
    id:int
    name:str
    last_name:str
    second_last_name:str
    photo_url:str
    email:str
    id_user:int