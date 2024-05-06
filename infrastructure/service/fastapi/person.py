from domain.entity.pydantic.person import PersonEntity
from application.person import PersonApplication
#from infrastructure.repository.mysql import person as personDB
import uvicorn
from fastapi import FastAPI, Request

__app_layer = None

apiServer = FastAPI()


if __name__ == "__main__":
    uvicorn.run(apiServer, host="0.0.0.0")

def PersonServiceFastApi(app:PersonApplication):
    global __app_layer
    __app_layer = app

    uvicorn.run(apiServer, host="0.0.0.0")


@apiServer.get("/person/list")
def List():
    global __app_layer
    return __app_layer.List()

@apiServer.post("person")
def Create(person:PersonEntity):
    global __app_layer
    return __app_layer.Create(person)

@apiServer.get("/")
def index():
    return "Hello world"