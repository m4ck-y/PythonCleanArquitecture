from application.person import PersonApplication
from infrastructure.repository.sql_alquemy.person import PersonRepositorySQLAlcchemy
from infrastructure.service.fastapi.person import PersonServiceFastApi

from fastapi import FastAPI
import uvicorn

def main():
    apiServer = FastAPI()

    repo = PersonRepositorySQLAlcchemy()
    application = PersonApplication(repo)
    service = PersonServiceFastApi(application, apiServer)

    from application.user import UserApplication
    from infrastructure.repository.sql_alquemy.user import UserRepositorySQLAlcchemy
    from infrastructure.service.fastapi.user import UserServiceFastApi
    
    userRepo = UserRepositorySQLAlcchemy()
    userApp = UserApplication(userRepo)
    userService = UserServiceFastApi(userApp, apiServer)

    from infrastructure.service.fastapi.admin import AdminServiceFastApi
    auth = AdminServiceFastApi(apiServer)

    uvicorn.run(apiServer, host="0.0.0.0")

if __name__ == "__main__":
    main()