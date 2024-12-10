
def web_scraper ():
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    from datetime import datetime
    import random
    import time

    now = datetime.now()

    formatted_datetime = now.strftime("%Y_%m_%d_%H_%M_%S") 
    #print("Current Time =", formatted_datetime)

    pd.set_option('display.max_rows', None)
    url = "https://www.nordnet.no/market/stocks?selectedTab=overview&exchangeCountry=NO"

    time.sleep(random.randint(1,3))
    page = requests.get(url, verify=False)

    soup = BeautifulSoup(page.text, "html.parser")

    main ={}
    list_name = []

    
    if page.status_code == 200:
        
        #print()
        divs = soup.find("div", role = "table")
        counter = -1
        for div in divs:
            nesteddict = {}
            
            counter = counter + 1
            textcounter = -1
            if counter == 0:
                for text in div:
                    names_text = text.get_text(strip=True)
                   #print("{0} hie".format(names_text))
                    list_name.append(names_text)

        
            if counter != 0:
                for text in div:
                            textcounter = textcounter + 1
                            #print(textcounter)
                            text_strip = text.get_text(strip=True)
                            
                            name = list_name[textcounter]
                            #print(name)

                            nesteddict[name] = text_strip
            #print(nesteddict)

            name_dict = None
            nesteddict_counter = -1 
            for key, value in nesteddict.items():
                 nesteddict_counter =  nesteddict_counter + 1
                 if nesteddict_counter == 1:
                      name_dict = value
                      #print(value)
                 #print(key, value) 
                           
            main[name_dict] = nesteddict
            #print(main)
                             
                
        df = pd.DataFrame.from_dict(main, orient="index")
        df.to_csv('csv_file/output_time_is_{0}.csv'.format(formatted_datetime), index=False)  
        #print(df)
    else:
        print("Error retrieving data from Nordnet, status code is{0}".format(page.status_code))
    
    """ for key, value in main.items():
        print("{0}, {1}".format(key, value))    """

web_scraper()