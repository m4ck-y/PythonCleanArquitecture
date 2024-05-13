from domain.entity.pydantic.user import UserEntity as E
from application.user import UserApplication

from fastapi import FastAPI, APIRouter, HTTPException


__app:UserApplication = None

ROUTE = "user"

apiRouter = APIRouter(prefix=f"/{ROUTE}", tags=[ROUTE])

def UserServiceFastApi(app:UserApplication, api_server:FastAPI):
    global __app
    __app = app
    api_server.include_router(apiRouter)

@apiRouter.get("/")
def index():
    return "User"

@apiRouter.get("/List/")
def List():
    return __app.List()

@apiRouter.get("/{id}")
def Get(id:int):
    return __app.Get(id)

@apiRouter.post("/")
def Create(value:E):
    return __app.Create(value)

@apiRouter.put("/")
def Update(value:E):
    return __app.Update(value)

@apiRouter.delete("/")
def Delete(id:int):
    return __app.Delete(id)

@apiRouter.get("/error/", status_code=201)
def error():
    return HTTPException(404, detail="Not Found")
    
@apiRouter.get("/error_ex/", status_code=201)
def error():
    raise HTTPException(404, detail="Not Found")
    