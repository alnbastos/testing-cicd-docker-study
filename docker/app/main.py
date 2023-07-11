from fastapi import FastAPI
from app.schemas import Animals
from app.database import Postgres

app = FastAPI()
database = Postgres()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.post("/create/animal/")
def create_animal(animal: Animals):
    dict_animal = dict(animal)
    database.insert_data(
        name=dict_animal["name"],
        species=dict_animal["species"],
        average_weight_kg=dict_animal["average_weight_kg"],
        country_origin=dict_animal["country_origin"],
        average_age=dict_animal["average_age"],
        photo=dict_animal["photo"]
    )

