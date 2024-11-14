import json
from bs4 import BeautifulSoup
import requests

json_file = "info.json"
url = "https://www.nordnet.no/market/stocks?selectedTab=overview&exchangeCountry=NO"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

#print(soup.prettify())





names = []
# Find the table with the stock information

div = soup.find_all("div", role="table")
rows = soup.find_all( role="row")
data_list = ()

data_lists = {
    
}
thisdict = {
    "row":  "{}"
}
#print(rows[0].get_text().strip())


rows0 = rows[0]
rows0span = rows0.find_all("span")


for span in rows0span:
        span_text = span.get_text().strip()
        names.append(span_text)
#for span in rows0span:
     #rows0span0 = span[0].get_text().strip()
     #print(span.get_text().strip())

for row in rows:
    i = 0
    # Find all span elements in each row
    spans = row.find_all("span")
    
    # Extract and print or store the text content from each span
    for span in spans:
          

          
       
        
#print (data_list)   


with open(json_file, "w") as file:
    json.dump(thisdict, file)
            
#print(div.prettify())
#print (div)
"""
for row in div:
    print(row)
    for i in row:
        print(i)
"""