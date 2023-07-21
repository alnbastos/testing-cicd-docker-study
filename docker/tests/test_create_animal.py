import pytest, requests, json

class TestCreateAnimal:
    def test_create_animal_valid(self):
        data = {
            "name": "Elefante",
            "species": "Loxodonta africana",
            "average_weight_kg": 6000.0,
            "country_origin": "África",
            "average_age": 70,
            "photo": "str"
        }
        result = requests.post("http://127.0.0.1:8000/create/animal/", data=json.dumps(data))
        assert result.status_code == 200