

def csv_scanner ():
    from python_folder.append_path import append_paths
    append_paths() 
    import os
    from datetime import datetime, timedelta

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

    now = datetime.now()

    year_now = now.year
    month_now = now.month
    day_now = now.day
    hour_now = now.hour
    minute_now = now.minute
    second_now = now.second
    date_time_obj_now = datetime(year_now, month_now, day_now, hour_now, minute_now, second_now)
    #print(date_time_obj_now)
    #print (formatted_datetime)

    difference_list = []

    filecount = -1
    for file in all_files_name:
        filecount += 1

        split_result_1 = file.split('_')
        year = int(split_result_1[3])
        month = int(split_result_1[4])
        day = int(split_result_1[5])
        hour = int(split_result_1[6])
        minute = int(split_result_1[7])
        second = int(split_result_1[8].replace('.csv', '')) 

        date_time_obj = datetime(year, month, day, hour, minute, second)
        difference = date_time_obj_now - date_time_obj
        #print(difference)
        difference_list.append(difference)
        
        if difference > timedelta(hours=2):
            all_files_count = all_files[filecount]
            os.remove(all_files_count)
            print(f"The file is more than 2 hours old. Difference: {difference}, {all_files_count}")
    #print(difference_list)


    

csv_scanner ()