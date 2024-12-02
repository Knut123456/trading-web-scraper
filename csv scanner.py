import os
from datetime import datetime

all_files_name =[]
all_files =[]
def finn_alle_filer(filepath):
    if os.path.exists(filepath):
        print("file exits")  
        with os.scandir(filepath) as files:
            for file in files:
                all_files.append(file.path)
                all_files_name.append(file.name)
                
    if os.path.exists(filepath) == False:
        print("file does not exist")
    if len(all_files) == 0:
        print("No files found in this directory")
    if len(all_files) > 0:
        print(all_files) 

finn_alle_filer("csv_file")

now = datetime.now()

formatted_datetime = now.strftime("%Y-%m-%d-%H-%M-%S")

print (formatted_datetime)
for file in all_files_name:
    split_result_1 = file.split('_')
    split_result_2 = [item.split('.') for item in split_result_1]
    for index,value in enumerate(split_result_2):
        print("{0}, {1}".format(index, value))


    #print(date_time_str_split)
    #if date_time_str


