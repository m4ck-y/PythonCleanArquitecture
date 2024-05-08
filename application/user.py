from domain.repository.user import UserRepository
from domain.entity.base.user import UserEntity

class UserApplication:

    def __init__(self, repository:UserRepository) -> None:
        self.repository = repository

    def Create(self, user:  UserEntity):
        return self.repository.Create(user)

    def Get(self, id:int):
        return self.repository.Get(id)

    def List(self):
        return self.repository.List()
    
    def Update(self, user:UserEntity):
        return self.repository.Update(user)

    def Delete(self, id):
        return self.repository.Delete(id)