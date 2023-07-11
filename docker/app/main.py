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


@app.get("/read/animal/")
def read_animal():
    list_animals = list()
    for data in database.read_data():
        list_animals.append({
            "id": data[0],
            "name": data[1],
            "species": data[2],
            "average_weight_kg": data[3],
            "country_origin": data[4],
            "average_age": data[5],
            "photo": data[6]
        })

    return list_animals

