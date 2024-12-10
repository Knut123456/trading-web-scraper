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

    what_i_want = ['Navn', 'I dag %', 'Siste', 'I dag +/-', 'I dag', 'Omsetning', 'Børsverdi']
    pd_file = pd.read_csv(file)
    #print(pd_file)
    

    
   # print(what_i_want)
    now = datetime.now()

    formatted_datetime = now.strftime("%Y_%m_%d_%H_%M_%S") 
    
    print(formatted_datetime)
    table_name = f"akjse_table_made_{formatted_datetime} "

    print(table_name)
    conn = connect_to_database()

    cursor = conn.cursor()



    def decide_column_type(column):
        if column.strip() in ["Navn", "Børsverdi", "I dag +/-"]:
            return "VARCHAR(255)"  # Use VARCHAR for textual or mixed data
        else:
            return "FLOAT"  # Use FLOAT for numeric data
        
    formatted_list_with_types = [f"`{column.strip()}` {decide_column_type(column)}" for column in what_i_want]
            
    print(what_i_want)
    create_table_query = f"""
        CREATE TABLE {table_name}(
        id INT AUTO_INCREMENT PRIMARY KEY, 
         {',\n    '.join(formatted_list_with_types)}
        );
        """
    
    print(create_table_query)  
    cursor.execute(create_table_query)
   
    for index, row in pd_file.iterrows():
            what_i_want_info = row[what_i_want]


    key_list = []
    value_list = []
    
    for key, value in what_i_want_info.items():
        key_type = decide_column_type(key)

        # Process based on type
        if key_type == "VARCHAR(255)":
            key_list.append(f"`{key}`")  # Add key to list with backticks
            value_list.append(f"'{value}'")  # Add value with single quotes for strings
        elif key_type == "FLOAT":
            key_list.append(f"`{key}`")  # Add key to list with backticks
            value_list.append(value)  # Add numeric value as is (no quotes)

    # Convert lists to strings
    
    key_list_str = ", ".join(key_list)
    print(key_list_str)
    key_type = decide_column_type(key_list_str)
    value_list_str = ", ".join(map(str, value_list))  # Ensure all values are strings

    # Construct the SQL query
    insert_table_query = f"INSERT INTO {table_name} ({key_list_str}) VALUES ({value_list_str});"

    # Construct the SQL query
    print(insert_table_query)   
    cursor.execute(insert_table_query)
    
    #print(cursor)


    conn.close()

csv_file_to_database()