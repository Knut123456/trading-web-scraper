def csv_file_to_database():
    import os
    import pandas as pd
    from datetime import datetime
    from connect_to_database import connect_to_database

    all_files_name =[]
    all_files =[]

    def finn_alle_filer(filepath):
            if os.path.exists(filepath):
                with os.scandir(filepath) as files:
                    for file in files:
                        all_files.append(file.path)
                        all_files_name.append(file.name)
                        
            if os.path.exists(filepath) == False:
                print("file does not exist")
            if len(all_files) == 0:
                print("No files found in this directory")

    finn_alle_filer("csv_file")

    stamp = "stamp"
    file_name = "file_name"
    timestamp = {}
    # get the timestamp
    for file in all_files:
        gettime = os.path.getmtime(file)
        timestamp[file_name] = file
        timestamp[stamp] = gettime


    #print(timestamp)

    timestamp_stamp = [timestamp[stamp]]
    timestamp_only = max(timestamp_stamp)

    #print(timestamp.items())

    for key, value in timestamp.items():
        if value == timestamp_only:
            # If the value matches, print the corresponding file_name
            file =timestamp['file_name']

    pd.set_option('display.max_rows', None)

    pd.set_option('display.max_columns', None)

    what_i_want = ['Navn',  'Siste',  'Omsetning', 'Børsverdi']
    pd_file = pd.read_csv(file)
    #print(pd_file)
    

    table_name = None
   # print(what_i_want)
    now = datetime.now()

    formatted_datetime = now.strftime("%Y_%m_%d_%H_%M_%S") 
    
    #print(formatted_datetime)
    table_name = f"akjse_table_made_{formatted_datetime}"

    #print(table_name)
    conn = connect_to_database("trading_web_scraper")

    cursor = conn.cursor()



    def decide_column_type(column):
        if column.strip() in ["Navn","Siste","Omsetning","Børsverdi"]:
            return "VARCHAR(255)"  # Use VARCHAR for textual or mixed data
        
    formatted_list_with_types = [f"`{column.strip()}` {decide_column_type(column)}" for column in what_i_want]
            
    #print(what_i_want)
    create_table_query = f"""
        CREATE TABLE {table_name}(
        id INT AUTO_INCREMENT PRIMARY KEY, 
         {',\n    '.join(formatted_list_with_types)}
        );
        """
    
    #print(create_table_query)  
    cursor.execute(create_table_query)
    for index, row in pd_file.iterrows():
        what_i_want_info = row[what_i_want]


        
        temp_dict_key = {} 
        temp_dict_value = {} 
       
        for key, value in what_i_want_info.items():
            temp_dict_key[key] = key
            value = value.replace("\xa0", ".")
    
            temp_dict_value[key] = value
        
        keys = temp_dict_key.values()
        
        #print()
    
        value_listsort = []

 
        for key, value in temp_dict_value.items():
            types = decide_column_type(key)
            #print(types)
            value_list = [value, types]
            value_listsort.append(value_list)
 

        values = []
        
       

        for (value, value_type) in value_listsort:
                values.append(f"'{value}'")
        
        
        insert_statement = f"""INSERT INTO {table_name} ({",".join(keys)}) VALUES ({",".join(values)});"""
        #print(insert_statement)
        

        cursor.execute(insert_statement)
        
   
    #print(values_dict)
    conn.commit()  
    conn.close()

    new_table_name = table_name
    return new_table_name

csv_file_to_database()