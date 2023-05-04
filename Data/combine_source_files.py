#ISYE 6740 Project Source code
#Created by: Miranda and Sabado

import pandas as pd
import os
import warnings
warnings.filterwarnings("ignore")

# Set the path to the folder where the CSV files are stored
# combine multiple csv files for both flight and weather into 2 csv files

# folder_path = "C:/project_data/flight"
folder_path = "C:/project_data/weather"

# Get a list of all the CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

print ("file names")
print (csv_files)

# Create an empty list to store the dataframes
dfs = []

print ("append csv to data frame")
# Loop through each CSV file and append the dataframe to the list
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    dfs.append(df)

print ("save to file")
# Concatenate all the dataframes into one
combined_df = pd.concat(dfs, ignore_index=True)

# Set the threshold to drop columns with 50% NaN values
thresh = len(combined_df) * 0.5

# Drop columns with NaN values greater than the threshold
combined_df = combined_df.dropna(thresh=thresh, axis=1)
#combined_df.to_csv('full_flight_data.csv')
combined_df.to_csv('weather.csv')

print ("complete")