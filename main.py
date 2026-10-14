from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict

from engine import Engine

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

class CatOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    age: int


@app.get("/allcats", response_model=list[CatOut])
async def all_cats():
    engine = Engine()
    return engine.print_cats()