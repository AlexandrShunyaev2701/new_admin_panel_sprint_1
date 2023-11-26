import uuid
from dataclasses import dataclass
import datetime as dt


@dataclass
class FilmWork:
    id: uuid.UUID
    title: str
    description: str
    creation_date: dt.datetime
    file_path: str
    rating: float
    type: str
    created_at: dt.datetime
    updated_at: dt.datetime



@dataclass
class Genre:
    id: uuid.UUID
    name: str
    description: str
    created_at: dt.datetime
    updated_at: dt.datetime


@dataclass
class Person:
    id: uuid.UUID
    full_name: str
    created_at: dt.datetime
    updated_at: dt.datetime


@dataclass
class PersonFilmWork:
    id: uuid.UUID
    film_work_id: uuid.UUID
    person_id: uuid.UUID
    role: str
    created_at: dt.datetime



@dataclass
class GenreFilmWork:
    id: uuid.UUID
    film_work_id: uuid.UUID
    genre_id: uuid.UUID
    created_at: dt.datetime
