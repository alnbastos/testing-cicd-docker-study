# from psycopg2.errors import DuplicateTable
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv('HOST_DB')
PORT = os.getenv('PORT_DB')
USER = os.getenv('USER_DB')
PASSWORD = os.getenv('PASSWORD_DB')
DATABASE = os.getenv('NAME_DB')

class Postgres:
    def __init__(self):
        self.connection = psycopg2.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE)
        self.cursor = self.connection.cursor()

    def create_table(self):
        sql = """
            CREATE TABLE animals (
                id SERIAL PRIMARY KEY,
                name VARCHAR(20),
                species VARCHAR(20),
                average_weight_kg FLOAT,
                country_origin VARCHAR(20),
                average_age INTEGER,  
                photo VARCHAR(50)
            );
        """
        self.cursor.execute(sql)

    def insert_data(self, name:str, species:str, average_weight_kg:float, country_origin:str, average_age:int, photo=None):
        sql = f"""
            INSERT INTO animals (name, species, average_weight_kg, country_origin, average_age, photo) \
            VALUES ('{name}', '{species}', '{average_weight_kg}', '{country_origin}', '{average_age}', 'gato.jpg');
        """
        self.cursor.execute(sql)
        self.connection.commit()
        self.close_connection()

    def read_data(self):
        sql = "SELECT * FROM animals"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        self.close_connection()

        return result, [column[0] for column in self.cursor.description]

    def close_connection(self):
        self.connection.close()
