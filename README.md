# Trading Web Scraper

## Innholdsfortegnelse
- [Velkommen til mitt prosjekt](#velkommen-til-mitt-prosjekt)
- [Funksjoner](#funksjoner)
- [Komme i gang](#komme-i-gang)
  - [Miljøvariabler](#miljøvariabler)
  - [Opprettelse av brukere](#opprettelse-av-brukere)
- [Installasjon](#installasjon)
- [Hvordan bruke boten](#hvordan-bruke-boten)
- [Merk](#merk)
- [Bidra](#bidra)
- [Kontakt](#kontakt)

## Velkommen til mitt prosjekt!

Dette prosjektet er en **trading bot** som kombinerer en web scraper for å hente markedsdata og putter disse informasjon til en nettside

## Funksjoner


- **Web Scraping**: Henter markedsdata fra forskjellige nettsteder i sanntid.
- **SQL Database**: Bruker en SQL-database til å lagre informasjon om brukere, trading-data og historikk.

## create database

Dersom du ønsker å bruke denne trading boten selv, må du sette opp en SQL-database og lage brukerkontoer for **admin** og **vanlige brukere**. Dette gir forskjellige tilgangsnivåer til funksjonene og dataene som brukes i boten.

need to have a mariadb database
in linux you need to  

   on linux you need to
   ```sh
   sudo apt install mariadb 
   ```
   then to 
### Miljøvariabler

For at applikasjonen skal fungere korrekt, må du sette opp følgende miljøvariabler i en `.env`-fil:

```env
DB_HOST= IP address
DB_USER= username
DB_PASSWORD= password
DB_NAME= database name
PORT= database port(usally 3306)
```

må ha for en annen database 
```env
DB_HOST_2 = IP address
DB_USER_2 =username
DB_PASSWORD_2 = password
DB_NAME_2 = database name
port_U2 = database port(usally 3306)
```

dette gjelder for begge databasene
- **DB\_HOST**: IP-adressen til databasen din.
- **DB\_USER**: Brukernavn for normal bruker av databasen. Det anbefales å opprette en egen bruker med begrensede rettigheter.
- **DB\_PASSWORD**: Passord for denne brukeren.
- **DB\_NAME**: Navnet på databasen som brukes til å lagre dataene.
- **PORT**: Portnummeret for å koble til databasen (standard er 3306).

### Opprettelse av brukere

- Brukeropprettelse
- Admin og normal bruker

Det anbefales å opprette to brukere i databasen:

1. **Admin-bruker**: Med full tilgang til alle tabeller og funksjoner.
2. **Normal bruker**: Med begrenset tilgang, som kun kan lese dataene og utføre operasjoner som ikke er kritiske.

Dette gir bedre sikkerhet og kontroll, spesielt når det gjelder datatilgang.

## Installasjon

- Installasjon
- Klon prosjektet
- Avhengigheter

1. **Klone prosjektet**:

   ```sh
   git clone https://github.com/Knut123456/trading-web-scraper.git
   cd trading-web-scraper
   ```

2. **Installer avhengigheter**:
   Kør følgende kommando for å installere nødvendige Python-pakker:
   vis du vil ha venv slik at dette ikke påvireker med andre proskjekter

   env_name kan du endre 
   ```sh
   python -m venv env_name
   ```
   windeos så gjør du 
   ```sh
   env_name\Scripts\activate.bat
   ```

   og på linux
   ```sh
   source env_name/bin/activate
   ```
   dette må du ha for at det skal fungere.

   vis du vil ha det på venv så må du ha det activated når du gjør det
   ```sh
   pip install -r requirements.txt
   ```

   når du er ferdig med venv filen 
   ```sh
   deactivate
   ```


3. **Sett opp miljøvariabler**:
   Opprett en `.env`-fil i rotkatalogen og legg til informasjonen som vist tidligere.

4. **Koble til databasen**:
   Forsikre deg om at du har riktig tilgang til databasen som spesifisert i `.env`-filen.

## Hvordan bruke boten

- **Start boten** ved å kjøre hovedfilen:
  ```sh
  python .\flask\python_app.py
  ```
- Etter oppstart vil boten hente markedsdata fra forskjellige nettsteder og gi deg oppdatert informasjon.

## Merk

- **Sikkerhet**: Ikke del `.env`-filen med sensitive detaljer. Beskytt den mot uautorisert tilgang.
- **Bruk ansvarlig**: Denne trading boten er kun for demonstrasjonsformål. Bruk av investeringsverktøy innebærer risiko, og du bør ikke investere uten å forstå risikoen.


## Kontakt



Hvis du har noen spørsmål eller tilbakemeldinger, ta gjerne kontakt med meg via [GitHub-profil](https://github.com/Knut123456)

Takk for at du sjekker ut mitt prosjekt, og lykke til med tradingen!

