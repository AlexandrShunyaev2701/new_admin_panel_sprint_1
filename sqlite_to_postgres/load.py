import os
import psycopg2
from dataclasses import *
from dataclas import FilmWork, Genre, Person, GenreFilmWork, PersonFilmWork
from save_sqlite import sqlite_extractor
from dotenv import load_dotenv


load_dotenv()


DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_OPTIONS = os.environ.get('DB_OPTIONS')

dsn = {
    'dbname': DB_NAME,
    'user': DB_USER,
    'password': DB_PASSWORD,
    'host': DB_HOST,
    'port': int(DB_PORT),
    'options': DB_OPTIONS,
}


def postgres_saver():
    dataclasses = {'film_work': FilmWork,'genre' :Genre,'genre_film_work': GenreFilmWork,'person': Person,'person_film_work': PersonFilmWork}
    with psycopg2.connect(**dsn) as conn, conn.cursor() as cursor:
        for table_name, model in dataclasses.items():
            result = sqlite_extractor(table_name)
            instance = model(**dict(result[0]))
            column_name = [field.name for field in fields(instance)]
            column_names_str = ','.join(column_name)
            col_count = ', '.join(['%s'] * len(column_name))   
            args = ','.join(cursor.mogrify(f"({col_count})", item).decode() for item in result)
            cursor.execute(f"""
            INSERT INTO {table_name} ({column_names_str})
            VALUES {args}"""
            f""" ON CONFLICT (id) DO NOTHING
            """)