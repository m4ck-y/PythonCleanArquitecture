from domain.entity.pydantic.user import UserEntity
from application.user import UserApplication

from fastapi import FastAPI, APIRouter, HTTPException


__app:UserApplication = None

apiRouter = APIRouter(prefix="/user")

def UserServiceFastApi(app:UserApplication, api_server:FastAPI):
    global __app
    __app = app
    api_server.include_router(apiRouter)

@apiRouter.get("/")
def index():
    return "User"

@apiRouter.get("/error/", status_code=201)
def error():
    return HTTPException(404, detail="Not Found")
    
@apiRouter.get("/error_ex/", status_code=201)
def error():
    raise HTTPException(404, detail="Not Found")
    