# Shengtao Tony Hou
# April 27th, 2022

import sys
import os
import pandas as pd

def main(argv_list):
    csv_files = []
    for i in range(0, len(argv_list)):
        #check to see if path is valid
        if os.path.isfile(argv_list[i]):
            #check to see if the input files ends with .csv to ensure we are processing only csv files
            if argv_list[i][-4:] == '.csv':
                csv_files.append(argv_list[i])

    filename_list = []
    for path in csv_files:
         # return the rest of the filename from the path
        name_index = path.rfind('/')
        filename = path[name_index + 1:]
        filename_list.append(filename)

    if filename_list!=[]:
        # base of the file and we concat from here
        df = pd.read_csv(csv_files[0])
        if len(filename_list) > 1:
            # looping
            for i in range(len(csv_files)):
                df1 = pd.read_csv(csv_files[i])
                # Creating new column called filename
                df1['filename'] = filename_list[i]
                # concat the existing base and the newly added df
                df = pd.concat([df, df1])
            # Converting the combined data frame and exporting it to a csv file
            df.to_csv("./combiner.csv")
            return "success"
    else:
        return "nofile"

if __name__ == "__main__":
    argv_list = ['./fixtures/clothing.csv' ,'./fixtures/accessories.csv']
    main(argv_list)