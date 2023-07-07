from fastapi import FastAPI
from app.schemas import Animals

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/create/animal/")
def create_animal(animal: Animals):
    return dict(animal)

