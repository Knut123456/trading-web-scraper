import requests
from bs4 import BeautifulSoup



# URL til nettsiden
url = "https://www.nordnet.no/aksjer/kurser?selectedTab=overview&exchangeCountry=NO"

# Hent HTML-innholdet fra nettsiden, og ignorer sertifikatvalidering
response = requests.get(url, verify=False)

# Hvis forespørselen er vellykket
if response.status_code == 200:
     # Parse HTML-innholdet med BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    names =[]
    rows0= soup.find_all('div', class_="Flexbox__StyledFlexbox-sc-1ob4g1e-0 LSuXj Row__StyledRow-sc-1iamenj-0 VwsYk HeaderRow__StyledHeaderRow-sc-1vg8bsb-0 gTZnmf Header-sc-b707b0ca-0 bZlIwz")
    rows0pan = rows0.find_all("span")
    for text in rows0pan:
        row0_text = text.get_text().strip()
        names.append(row0_text)

    print(names)

    # Finn alle <div>-elementer med den spesifikke klassen
    div_elements = soup.find_all('div', class_="Flexbox__StyledFlexbox-sc-1ob4g1e-0")

    # Lag en liste med bare teksten fra hver <div>-tag (fjern HTML-tags)
    div_text_list = [div.get_text(strip=True) for div in div_elements]

    # Skriv ut listen med ren tekst (plain text)
    for text in div_text_list:
        print(text[0])
else:
    print(f"Feil ved henting av siden, statuskode: {response.status_code}")
