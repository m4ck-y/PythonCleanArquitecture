import uvicorn
from fastapi import FastAPI, Request


app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")