import json
from bs4 import BeautifulSoup
import requests

json_file = "info.json"
url = "https://www.nordnet.no/market/stocks?selectedTab=overview&exchangeCountry=NO"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

#print(soup.prettify())





info = []
rows =[]
# Find the table with the stock information

div = soup.find_all("div", role="table")
rows = soup.find_all( role="row")




for row in rows:
    #print(div[0])

     
    # Find all span elements in each row
  
    spans = row.find_all("span")
    # Extract and print or store the text content from each span
    for span in spans:
        row_data = [span.get_text().strip()]
        #row_data_sort = row_data.sort(separator=",")
        #row_data_1 = row_data_sort [0]
        print(row_data)
        # Append the row data to the rows list
        #info.append(row_data_sort)  
   

print(info)
with open(json_file, "w") as file:
    json.dump(info, file)
            
#print(div.prettify())
#print (div)
"""
for row in div:
    print(row)
    for i in row:
        print(i)
"""