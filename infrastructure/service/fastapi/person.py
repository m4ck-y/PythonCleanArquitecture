from domain.entity.pydantic.person import PersonEntity
from application.person import PersonApplication
#from infrastructure.repository.mysql import person as personDB
import uvicorn
from fastapi import FastAPI, Request

__app = None

apiServer = FastAPI()


def PersonServiceFastApi(app:PersonApplication):
    global __app
    __app = app

    uvicorn.run(apiServer, host="0.0.0.0")

@apiServer.get("/person/{id}")
def Get(id:int):
    r = __app.Get(id)
    return r

@apiServer.get("/person/list/")
def List():
    return __app.List() 

@apiServer.post("/person")
def Create(person:PersonEntity):
    return __app.Create(person)

@apiServer.put("/person")
def Update(person:PersonEntity):
    return __app.Update(person)

@apiServer.delete("/person")
def Delete(id:int):
    return __app.Delete(id)


if __name__ == "__main__":
    uvicorn.run(apiServer, host="0.0.0.0")

@apiServer.get("/")
def index():
    return "Hello world"