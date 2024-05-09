from application.person import PersonApplication
from infrastructure.repository.memory.person import PersonRepositoryMemory
from infrastructure.service.fastapi.person import PersonServiceFastApi

from fastapi import FastAPI
import uvicorn

def main():
    apiServer = FastAPI()

    repo = PersonRepositoryMemory()
    application = PersonApplication(repo)
    service = PersonServiceFastApi(application, apiServer)

    from application.user import UserApplication
    from infrastructure.repository.memory.user import UserRepositoryMemory
    from infrastructure.service.fastapi.user import UserServiceFastApi
    
    userRepo = UserRepositoryMemory()
    userApp = UserApplication(userRepo)
    userService = UserServiceFastApi(userApp, apiServer)

    from infrastructure.service.fastapi.admin import AdminServiceFastApi
    auth = AdminServiceFastApi(apiServer)

    uvicorn.run(apiServer, host="0.0.0.0")

if __name__ == "__main__":
    main()