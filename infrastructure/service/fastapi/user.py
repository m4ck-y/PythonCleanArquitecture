from domain.entity.pydantic.user import UserEntity
from application.user import UserApplication

from fastapi import FastAPI, APIRouter


__app:UserApplication = None

apiRouter = APIRouter(prefix="/user")

def UserServiceFastApi(app:UserApplication, api_server:FastAPI):
    global __app
    __app = app
    api_server.include_router(apiRouter)

@apiRouter.get("/")
def index():
    return "User"
    
