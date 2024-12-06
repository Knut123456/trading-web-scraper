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

- Trading bot

Dette prosjektet er en **trading bot** som kombinerer en web scraper for å hente markedsdata og analysere disse for å anbefale investeringer. Prosjektet er ment å automatisere beslutningsprosessen for trading ved å bruke oppdaterte data som er hentet fra ulike nettsteder.

## Funksjoner


- Web scraping

- **Web Scraping**: Henter markedsdata fra forskjellige nettsteder i sanntid.
- **SQL Database**: Bruker en SQL-database til å lagre informasjon om brukere, trading-data og historikk.

## Komme i gang


- Database oppsett

Dersom du ønsker å bruke denne trading boten selv, må du sette opp en SQL-database og lage brukerkontoer for **admin** og **vanlige brukere**. Dette gir forskjellige tilgangsnivåer til funksjonene og dataene som brukes i boten.

### Miljøvariabler

For at applikasjonen skal fungere korrekt, må du sette opp følgende miljøvariabler i en `.env`-fil:

```env
DB_HOST=10.100.10.142
DB_USER=trading_web_scraper_user_normal_user
DB_PASSWORD=4321
DB_NAME=trading_web_scraper
PORT=3306
```

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
   git clone https://github.com/dittbrukernavn/trading-web-scraper.git
   cd trading-web-scraper
   ```

2. **Installer avhengigheter**:
   Kør følgende kommando for å installere nødvendige Python-pakker:

   ```sh
   pip install -r requirements.txt
   ```

3. **Sett opp miljøvariabler**:
   Opprett en `.env`-fil i rotkatalogen og legg til informasjonen som vist tidligere.

4. **Koble til databasen**:
   Forsikre deg om at du har riktig tilgang til databasen som spesifisert i `.env`-filen.

## Hvordan bruke boten

- Brukerveiledning
- Start boten

- **Start boten** ved å kjøre hovedfilen:
  ```sh
  python main.py
  ```
- Etter oppstart vil boten hente markedsdata fra forskjellige nettsteder og gi deg oppdatert informasjon.

## Merk

- Viktige merknader
- Sikkerhet
- Ansvarlig bruk

- **Sikkerhet**: Ikke del `.env`-filen med sensitive detaljer. Beskytt den mot uautorisert tilgang.
- **Bruk ansvarlig**: Denne trading boten er kun for demonstrasjonsformål. Bruk av investeringsverktøy innebærer risiko, og du bør ikke investere uten å forstå risikoen.


## Kontakt

- Kontaktinformasjon

Hvis du har noen spørsmål eller tilbakemeldinger, ta gjerne kontakt med meg via [e-postadresse eller GitHub-profil].

Takk for at du sjekker ut mitt prosjekt, og lykke til med tradingen!

