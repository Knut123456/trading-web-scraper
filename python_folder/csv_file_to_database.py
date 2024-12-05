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


    pd_file = pd.read_csv(file)
    #print(pd_file)
    for index, row in pd_file.iterrows():
        what_i_want = ['Navn', 'I dag %', 'Siste', 'I dag +/-', 'I dag', 'Omsetning', 'Børsverdi']
        what_i_want_info = row[what_i_want]
        #print(what_i_want_info)

    

    now = datetime.now()

    year_now = now.year
    month_now = now.month
    day_now = now.day
    hour_now = now.hour
    minute_now = now.minute
    second_now = now.second
    date_time_obj_now = datetime(year_now, month_now, day_now, hour_now, minute_now, second_now)
    
    conn = connect_to_database()
    
    #print(cursor)



csv_file_to_database()