import json
from bs4 import BeautifulSoup
import requests
import time
import random

json_file = "info.json"
url = "https://www.nordnet.no/market/stocks?selectedTab=overview&exchangeCountry=NO"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

names = []

divs = soup.find("div", role = "table")
divs_len = len(divs)

print(divs_len)
for div in divs:
    div0 = div[0]
    if div == div0:
     for row in div:
        names.append(row)
    #print(div)
    div_text =div.get_text().strip()
    #print(div_text)
   
print(names)