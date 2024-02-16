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
INSERT INTO films (name, year, runtime) VALUES ('The Reluctant Dragon', 1941, 74);
INSERT INTO films (name, year, runtime) VALUES ('Song of the South', 1946, 94);
INSERT INTO films (name, year, runtime) VALUES ('Fun & Fancy Free', 1947, 73);
INSERT INTO films (name, year, runtime) VALUES ('Melody Time', 1948, 75);
INSERT INTO films (name, year, runtime) VALUES ('So Dear To My Heart', 1948, 82);
INSERT INTO films (name, year, runtime) VALUES ('The Adventures of Ichabod and Mr. Toad', 1949, 68);
INSERT INTO films (name, year, runtime) VALUES ('Cinderella', 1950, 74);
INSERT INTO films (name, year, runtime) VALUES ('Alice in Wonderland', 1951, 75);
INSERT INTO films (name, year, runtime) VALUES ('Peter Pan', 1953, 77);
INSERT INTO films (name, year, runtime) VALUES ('Lady and the Tramp', 1955, 76);
INSERT INTO films (name, year, runtime) VALUES ('Sleeping Beauty', 1959, 75);


