CREATE TABLE films (id SERIAL PRIMARY KEY, name TEXT, year INTEGER, runtime INTEGER);
CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT);
CREATE TABLE user_info  (id SERIAL PRIMARY KEY, user_id INREGER REFERENCES users, age INTEGER, favourite_film TEXT);
CREATE TABLE reviews (id SERIAL PRIMARY KEY, film_id INTEGER REFERENCES film, writer_id INTEGER REFERENCES users, review TEXT);
CREATE TABLE stars (id SERIAL PRIMARY KEY, film_id INTEGER REFERENCES, writer_id INTEGER REFERENCES users, stars INTEGER);
INSERT INTO films (name, year, runtime) VALUES ("Snow White and the Seven Dwarfs", 1937, 83);
INSERT INTO films (name, year, runtime) VALUES ("Pinocchio", 1940, 88);
INSERT INTO films (name, year, runtime) VALUES ("Fantasia", 1940, 125);
INSERT INTO films (name, year, runtime) VALUES ("Dumbo", 1941, 64);
INSERT INTO films (name, year, runtime) VALUES ("Bambi", 1942, 69);


