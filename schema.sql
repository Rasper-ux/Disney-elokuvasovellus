CREATE TABLE films (id SERIAL PRIMARY KEY, name TEXT, year INTEGER, runtime INTEGER);
CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT);
CREATE TABLE user_info  (id SERIAL PRIMARY KEY, user_id INTEGER REFERENCES users, age INTEGER, favourite_film TEXT);
CREATE TABLE reviews (id SERIAL PRIMARY KEY, film_id INTEGER REFERENCES films, writer_id INTEGER REFERENCES users, review TEXT, stars INTEGER);
CREATE TABLE alike (id SERIAL PRIMARY KEY, film1_id INTEGER REFERENCES films, film2_id INTEGER REFERENCES films);

INSERT INTO films (name, year, runtime) VALUES ('Snow White and the Seven Dwarfs', 1937, 83);
INSERT INTO films (name, year, runtime) VALUES ('Pinocchio', 1940, 88);
INSERT INTO films (name, year, runtime) VALUES ('Fantasia', 1940, 125);
INSERT INTO films (name, year, runtime) VALUES ('Dumbo', 1941, 64);
INSERT INTO films (name, year, runtime) VALUES ('Bambi', 1942, 69);
INSERT INTO films (name, year, runtime) VALUES ('Saludos Amigos', 1942, 42);
INSERT INTO films (name, year, runtime) VALUES ('The Three Caballeros', 1944, 71);
INSERT INTO films (name, year, runtime) VALUES ('Make Mine Music', 1946, 75);




