# Trading Web Scraper og AI Bot

## Velkommen til mitt prosjekt!

Dette prosjektet er en **trading bot** som kombinerer en web scraper og en AI-modell for å analysere markedsdata og anbefale investeringer. AI-en vil gi forslag til hva du burde investere i basert på de innsamlede dataene fra web scraperen. Prosjektet er ment å automatisere beslutningsprosessen for trading, ved å bruke oppdaterte data og maskinlæringsteknikker.

## Funksjoner
- **Web Scraping**: Henter markedsdata fra forskjellige nettsteder i sanntid.
- **AI-basert Analyse**: Bruker maskinlæring for å analysere dataene og gi investeringsanbefalinger.
- **SQL Database**: Bruker en SQL-database til å lagre informasjon om brukere, trading-data, og historikk.

## Komme i gang
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

- **DB_HOST**: IP-adressen til databasen din.
- **DB_USER**: Brukernavn for normal bruker av databasen. Det anbefales å opprette en egen bruker med begrensede rettigheter.
- **DB_PASSWORD**: Passord for denne brukeren.
- **DB_NAME**: Navnet på databasen som brukes til å lagre dataene.
- **PORT**: Portnummeret for å koble til databasen (standard er 3306).

### Opprettelse av brukere
Det anbefales å opprette to brukere i databasen:
1. **Admin-bruker**: Med full tilgang til alle tabeller og funksjoner.
2. **Normal bruker**: Med begrenset tilgang, som kun kan lese dataene og utføre operasjoner som ikke er kritiske.

Dette gir bedre sikkerhet og kontroll, spesielt når det gjelder datatilgang.

## Installasjon
1. **Klone prosjektet**:
   ```sh
   git clone https://github.com/dittbrukernavn/trading-web-scraper-and-ai.git
   cd trading-web-scraper-and-ai
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
- **Start boten** ved å kjøre hovedfilen:
  ```sh
  python main.py
  ```
- Etter oppstart vil boten hente markedsdata og utføre analyse for å gi deg investeringsforslag.

## Merk
- **Sikkerhet**: Ikke del `.env`-filen med sensitive detaljer. Beskytt den mot uautorisert tilgang.
- **Bruk ansvarlig**: Denne trading boten er kun for demonstrasjonsformål. Bruk av investeringsverktøy innebærer risiko, og du bør ikke investere uten å forstå risikoen.

## Bidra
Dersom du vil bidra til prosjektet, vennligst følg standard prosess for pull requests:
1. Fork repoet.
2. Lag en branch for dine endringer.
3. Lag en pull request med beskrivelser av hva du har gjort.

## Kontakt
Hvis du har noen spørsmål eller tilbakemeldinger, ta gjerne kontakt med meg via [e-postadresse eller GitHub-profil].

Takk for at du sjekker ut mitt prosjekt, og lykke til med tradingen!

