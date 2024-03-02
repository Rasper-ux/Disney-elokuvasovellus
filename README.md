# Disney-elokuvasovellus
Sovelluksessa näkyy luettelo Disneyn animaatioelokuvista, joista voi katsoa tietoa ja lukea arvioita.
- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä voi lisätä profiiliinsa tietoa, kuten ikänsä ja lempielokuvan, joita voi myöhemmin muokata.
- Käyttäjä näkee luettelon elokuvista julkaisuvuosineen ja kestoineen julkaisujärjestyksessä ja voi painaa elokuvasta, jolloin siitä näytetään lisää tietoa (muiden käyttäjien antamat arvosanat ja kirjalliset arvostelut, sekä samankaltaiset elokuvat).
- Arvostelun antajaa painamalla näkee tietoja arvostelijasta
- Käyttäjä voi etsiä elokuvia hakusanoilla nimen mukaan.
- Luettelon elokuvista voi myös järjestää elokuvien keston, arvosanan tai julkaisuvuoden mukaan.


Käynnistysohje:

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

DATABASE_URL=tietokannan paikallinen osoite

SECRET_KEY=salainen avain


Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla

$ python3 -m venv venv

$ source venv/bin/activate

$ pip install -r ./requirements.txt


Määritä vielä tietokannan skeema komennolla

$ psql < schema.sql


Nyt voit käynnistää sovelluksen komennolla

$ flask run
