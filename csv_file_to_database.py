import os
import pandas as pd
from csv_scanner import csv_scanner
from datetime import datetime

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

timestamp = []
# get the timestamp
for file in all_files:
    gettime = os.path.getmtime(file)
    timestamp.append(gettime)

for ts in timestamp:
    print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

pd.set_option('display.max_rows', None)

pd.set_option('display.max_columns', None)


#print (file_pd_read)
#file_pd_read.info()

#first_row = file_pd_read.iloc[:]
#print (first_row)
""" name = file_pd_read.at[ "Navn"]
age_of_bob = file_pd_read.at[ "Navn"]  """

