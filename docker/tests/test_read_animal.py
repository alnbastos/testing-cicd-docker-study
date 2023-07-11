import pytest, requests, json

class TestReadAnimal:
    def test_read_animal_valid(self):
        result = requests.get("http://127.0.0.1:8000/read/animal/")
        assert result.status_code == 200

