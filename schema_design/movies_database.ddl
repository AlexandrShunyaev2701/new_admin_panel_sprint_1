CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    creation_date DATE,
    file_path TEXT,
    rating FLOAT,
    type TEXT NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

CREATE TABLE content.genre(
    id uuid PRIMARY KEY,
    name text NOT NULL,
    description text,
    created_at timestamp with time zone,
    updated_at timestamp with time zone  
);

CREATE TABLE content.person(
    id uuid PRIMARY KEY,
    full_name text NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.person_film_work (
    id uuid PRIMARY KEY,
    film_work_id uuid  REFERENCES content.film_work (id),
    person_id uuid REFERENCES content.person (id),
    role TEXT NOT NULL, 
    created_at timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre_film_work (
    id uuid PRIMARY KEY,
    film_work_id uuid  REFERENCES content.film_work (id),
    genre_id uuid REFERENCES content.genre (id),
    created_at timestamp with time zone
);

CREATE UNIQUE INDEX film_work_person_idx ON content.person_film_work (film_work_id, person_id);
CREATE INDEX IF NOT EXISTS film_work_creation_date_idx ON content.film_work (creation_date);
CREATE INDEX IF NOT EXISTS film_work_rating_idx ON content.film_work (rating);
CREATE UNIQUE INDEX IF NOT EXISTS film_work_person_unique_idx ON content.person_film_work (film_work_id, person_id, role);
CREATE UNIQUE INDEX IF NOT EXISTS film_work_genre_unique_idx ON content.genre_film_work (film_work_id, genre_id);