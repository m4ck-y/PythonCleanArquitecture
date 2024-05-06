from datetime import datetime

class PersonEntity:

    def __init__(self,
                 id:int=0,
                 name:str="",
                 last_name:str="",
                 second_last_name:str="",
                 photo_url:str="",
                 birthdate: datetime=datetime.now(),
                 email:str="",
                 id_user:int=0
                 ) -> None:
        
        self.id = id
        self.name = name
        self.last_name = last_name
        self.second_last_name = second_last_name
        self.photo_url = photo_url
        self.birthdate = birthdate
        self.email = email
        self.id_user = id_user