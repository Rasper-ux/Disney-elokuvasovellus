# Disney-elokuvasovellus
Sovelluksessa näkyy luettelo vuodesta 1937 nykypäivään julkaistuista Disneyn animaatioelokuvista, joista voi etsiä tietoa ja lukea arvioita. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.
- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä voi lisätä profiiliinsa tietoa, kuten käyttäjänimen, syntymäpäivän ja lempielokuvan.
- Käyttäjä näkee luettelon elokuvista julkaisuvuosineen aakkosjärjestyksessä ja voi painaa elokuvasta, jolloin siitä näytetään lisää tietoa (esimerkiksi kesto, genret, muiden käyttäjien antamat arvosanat ja kirjalliset arvostelut).
- Ylläpitäjä voi tarvittaessa poistaa käyttäjän antaman arvion sekä määrittää elokuvista näytettävät tiedot.
- Käyttäjä voi etsiä elokuvia, esim. keston, arvosanan tai julkaisuvuoden mukaan.
- Luettelon elokuvista voi myös järjestää elokuvien keston, arvosanan tai julkaisuvuoden mukaan.

Tällä hetkellä sovelluksessa toimii kirjautuminen ja uuden tunnuksen luominen. Lisäksi aloitussivulla näkyy lista elokuvista (vielä vain osa niistä).


Käynnistysohje:

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

DATABASE_URL=<tietokannan-paikallinen-osoite

SECRET_KEY=<salainen-avain


Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla

$ python3 -m venv venv

$ source venv/bin/activate

$ pip install -r ./requirements.txt


Määritä vielä tietokannan skeema komennolla

$ psql < schema.sql


Nyt voit käynnistää sovelluksen komennolla

$ flask run
