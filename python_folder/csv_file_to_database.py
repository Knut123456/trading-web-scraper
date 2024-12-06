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
    for index, row in pd_file.iterrows():
        what_i_want_info = row[what_i_want]
        print(what_i_want_info)

    
    print(what_i_want)
    now = datetime.now()

    formatted_datetime = now.strftime("%Y_%m_%d_%H_%M_%S") 
    
    print(formatted_datetime)
    table_name = f"akjse_table_made_{formatted_datetime} "

    print(table_name)
    conn = connect_to_database()

    cursor = conn.cursor()

    

    for table in what_i_want:
        table_info_info =f" {table},"

        
    
    
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {table_name}(
        id INT AUTO_INCREMENT PRIMARY KEY   

        );
        """
    for table in what_i_want:
        table_info_info =f" {table},"
        add_column_query = f"""
            ALTER TABLE {table_name}
            ADD COLUMN {table};
            """
        cursor.execute(add_column_query)

    print(create_table_query)  
    cursor.execute(create_table_query)
    
    #print(cursor)


    conn.close()


csv_file_to_database()