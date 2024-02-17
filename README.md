# Disney-elokuvasovellus
Sovelluksessa näkyy luettelo vuodesta 1937 nykypäivään julkaistuista Disneyn animaatioelokuvista, joista voi etsiä tietoa ja lukea arvioita.
- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä voi lisätä profiiliinsa tietoa, kuten käyttäjänimen, syntymäpäivän ja lempielokuvan.
- Käyttäjä näkee luettelon elokuvista julkaisuvuosineen julkaisujärjestyksessä ja voi painaa elokuvasta, jolloin siitä näytetään lisää tietoa (esimerkiksi kesto, muiden käyttäjien antamat arvosanat ja kirjalliset arvostelut).
- Käyttäjä voi etsiä elokuvia, esim. keston, arvosanan tai julkaisuvuoden mukaan.
- Luettelon elokuvista voi myös järjestää elokuvien keston, arvosanan tai julkaisuvuoden mukaan.

Tällä hetkellä sovelluksessa toimii:
- kirjautuminen ja uuden tunnuksen luominen
- aloitussivulla näkyy lista elokuvista (vielä vain osa niistä)
- kirjautumisen jälkeen käyttäjä voi lisätä elokuvan sivulla elokuvalle arvostelun
- elokuvan sivulla näkyy (vielä vain osassa) samankaltaiset elokuvat


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
