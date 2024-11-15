import json
from bs4 import BeautifulSoup
import requests
import time
import random

json_file = "info.json"
url = "https://www.nordnet.no/market/stocks?selectedTab=overview&exchangeCountry=NO"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

#print(soup.prettify())
spandict={}




names = []

# Find the table with the stock information

div = soup.find_all("div", role="table")
rows = soup.find_all("div", role="row")

thisdict = {
    
}
#print(rows[0].get_text().strip())


rows0 = rows[0]
rows0pan = rows0.find_all("span")


#rows1 = rows[1]
#rows1_div = rows1.find_all("div")
#rows1pan = rows1_div.find(text=True)


for text in rows0pan:
    row0_text = rows0pan.get_text().strip()
    names.append(row0_text)


print (names)
#for span in rows0span:
     #rows0span0 = span[0].get_text().strip()
     #print(span.get_text().strip())
rowcheck = True
for row in rows:
    #time.sleep(random.randint(1,3))
    # Find all span elements in each row
    divs = row.find_all("div")
    texts = div.find_all(text = True)
    
    rowdict = {}
    if rowcheck == True:
        print("row is working")
    rowcheck = False
    # Extract and print or store the text content from each span
    for div in divs:
        for text in texts:
            for index, value in enumerate(texts):
                name = names[index]
                rowdict[name] = span_text
            
                span_text = span.get_text().strip()
                    

                    #print(f"Index: {index}, Value: {value}")
                    #print ("for span loop is working")
                

    thisdict["row1"] = rowdict
    

print(thisdict)        

          
       
        
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