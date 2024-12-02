
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

now = datetime.now()

formatted_datetime = now.strftime("%Y_%m_%d_%H_%M_%S") 
print("Current Time =", formatted_datetime)

pd.set_option('display.max_rows', None)
json_file = "info.json"
url = "https://www.nordnet.no/market/stocks?selectedTab=overview&exchangeCountry=NO"

page = requests.get(url, verify=False)

soup = BeautifulSoup(page.text, "html.parser")

lists = []



divs = soup.find("div", role = "table")
for div in divs:
    for text in div:
        text_strip = div.get_text(strip=True)

    lists.append(text_strip)
    #rint(text_strip)

    
#print(lists)
df = pd.DataFrame(lists, columns=['Text'])


df.to_csv('csv_file/output_time_is_{0}.csv'.format(formatted_datetime), index=False)  
#print(df)