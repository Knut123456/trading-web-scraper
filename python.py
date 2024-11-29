
from bs4 import BeautifulSoup
import requests
import pandas as pd


pd.set_option('display.max_rows', None)
info_dict = {
    
}
json_file = "info.json"
url = "https://www.nordnet.no/market/stocks?selectedTab=overview&exchangeCountry=NO"

page = requests.get(url, verify=False)

soup = BeautifulSoup(page.text, "html.parser")

names = []

glem_index =[]

index = -1
divs = soup.find("div", role = "table")
for div in divs:
    text_index = -1
    name_index = -1
    index += 1
    row_dict ={}
    if index == 0 :
        for name in div:
            name_index += 1
            name_text = name.get_text().strip()
            names.append(name_text)
    #print(names)            
                 
            
    if index != 0 :
        for text in div:
            text_index += 1
            only_text=text.get_text().strip()
            info_dict[names[text_index]] = only_text
            


    
    #print(index)
#print(glem_index)
#print(names)
print(info_dict)