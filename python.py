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

main_div = soup.find("div", class_="FlexTable__StyledDiv-sc-v6wpic-0 gDVRVW")
rows = main_div.find_all("div", role="row")
rows_length = len(rows)
print(rows_length)

thisdict = {
    
}
#print(rows[0].get_text().strip())


rows0 = rows[0]
rows0pan = rows0.find_all("span")


#rows1 = rows[1]
#rows1_div = rows1.find_all("div")
#rows1pan = rows1_div.find(text=True)


for text in rows0pan:
    row0_text = text.get_text().strip()
    names.append(row0_text)

def find_child_nodes(node):
    # Finds all descendant nodes within the given node
    
   # for child in node.children

    #if child_nodes_length > 0:
       
    """    find_child_nodes(child_nodes)

    if child_nodes_length == 0:
        child_nodes_singel = node.find(recursive=True)
        text_content = child_nodes_singel.get_text(strip=True)
        print(text_content)
        #return text_content """
    
    

print (names)

rowcheck = True
for row in rows:
    #print(rows[2])
    divs = row.find_all("div", role ="columnheader")
    print(divs[0])
    #print(divs.get_text().strip()[0])
    rowdict = {}
    if rowcheck == True:
        print("row is working")
    rowcheck = False
    # Extract and print or store the text content from each span
    for div in divs:
        print(divs[0])
        #test = find_child_nodes(div)
        #print(test)
        #print(div.get_text().strip()[0])
        print(divs_children[0])
        tags_with_text = soup.find_all(lambda tag: tag.string and tag.string.strip())

        for tag in tags_with_text:
            print(f"Tag: {tag.name}, Text: {tag.string.strip()}")
    """     for text in texts: """
    """         for index, value in enumerate(texts): """
    """             name = names[index] """
    """             rowdict[name] = span_text """
    """          """
    """             span_text = text.get_text().strip()  """
                    

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