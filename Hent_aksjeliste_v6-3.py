import requests
from bs4 import BeautifulSoup
import pandas as pd

# Sett pandas til å vise alle rader
pd.set_option('display.max_rows', None)  # Sett til None for å vise alle radene

# URL til nettsiden
url = "https://www.nordnet.no/aksjer/kurser?selectedTab=overview&exchangeCountry=NO"

# Hent HTML-innholdet fra nettsiden, og ignorer sertifikatvalidering
response = requests.get(url, verify=False)

# Hvis forespørselen er vellykket
if response.status_code == 200:
    # Parse HTML-innholdet med BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Finn alle <div>-elementer med den spesifikke klassen
    div_elements = soup.find_all('div', class_="Flexbox__StyledFlexbox-sc-1ob4g1e-0")

    # Lag en liste med bare teksten fra hver <div>-tag (fjern HTML-tags)
    div_text_list = [div.get_text(strip=True) for div in div_elements]

        
    # Skriv ut listen med ren tekst (plain text)
    #for text in div_text_list:
        #print(text)
        
    # Lag en pandas DataFrame for å vise resultatet i tabellformat
    df = pd.DataFrame(div_text_list, columns=['Text'])
    
    # Fjern de første 117 radene og de siste 18 radene
    df = df.iloc[117:-18].reset_index(drop=True)

    
    #Skriver til fil.
    df.to_csv('output.csv', index=False)  
    # Lagre tabellen som CSV

    # Skriv ut tabellen
    print(df)
else:
    print(f"Feil ved henting av siden, statuskode: {response.status_code}")
