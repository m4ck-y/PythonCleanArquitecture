from domain.entity.pydantic.person import PersonEntity
from application.person import PersonApplication
#from infrastructure.repository.mysql import person as personDB
from fastapi import FastAPI, APIRouter

__app:PersonApplication = None

apiRouter = APIRouter()


def PersonServiceFastApi(app:PersonApplication, api_server:FastAPI):
    global __app
    __app = app
    api_server.include_router(apiRouter)

@apiRouter.get("/person/{id}")
def Get(id:int):
    r = __app.Get(id)
    return r

@apiRouter.get("/person/list/")
def List():
    return __app.List() 

@apiRouter.post("/person")
def Create(person:PersonEntity):
    return __app.Create(person)

@apiRouter.put("/person")
def Update(person:PersonEntity):
    return __app.Update(person)

@apiRouter.delete("/person")
def Delete(id:int):
    return __app.Delete(id)


if __name__ == "__main__":
    #uvicorn.run(apiRouter, host="0.0.0.0")
    print("NOT IMPLEMENTED")

@apiRouter.get("/")
def index():
    return "Hello world"