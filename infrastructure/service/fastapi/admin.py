#from domain.entity.pydantic.person import PersonEntity
#from application.person import PersonApplication
#from infrastructure.repository.mysql import person as personDB
from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from domain.entity.pydantic.user import UserEntity, UserDbEntity

#__app:PersonApplication = None

apiRouter = APIRouter(prefix="/admin")

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


def AdminServiceFastApi(api_server:FastAPI):#app:PersonApplication, api_server:FastAPI):
    """ global __app
    __app = app """
    api_server.include_router(apiRouter)

@apiRouter.get("/")
def index():
    return "Hello world"

userDB = {"name":"root", "pass":"123"}

def search_user(name:str):
    if name in userDB:
        return userDB

async def current_user(token:str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Not exists")

@apiRouter.post("/login")
async def login(form:OAuth2PasswordRequestForm = Depends()):
    
    if not(form.username == userDB["name"] and form.password == userDB["pass"]):
        raise HTTPException(400, detail="Not exists")
    
    return {"access_token":userDB["name"], "token_type": "bearer"}

@apiRouter.get("/me")
async def me(user:UserEntity = Depends(current_user)):
    return user


if __name__ == "__main__":
    #uvicorn.run(apiRouter, host="0.0.0.0")
    print("NOT IMPLEMENTED")
