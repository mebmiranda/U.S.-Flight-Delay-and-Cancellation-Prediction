#ISYE 6740 Project Source code
#Created by: Miranda and Sabado

#Merge flight and weather data into a single data frame which will be used for the analysis

import pandas as pd
import numpy as np
import os
import warnings
warnings.filterwarnings("ignore")

df_weather = pd.read_csv("C:\project_data\merged\weather_final.csv")
df_flight = pd.read_csv("C:\project_data\merged/flight_final.csv")

# reduce flight columns
# Specify columns to keep
# keep_columns = ['FL_DATE', 'ORIGIN', 'DEST', 'DEP_TIME', 'OP_CARRIER_FL_NUM']

# Drop all other columns
# df_flight = df_flight.drop(columns=[col for col in df_flight.columns if col not in keep_columns])

# Convert column to time format
df_flight['FL_DATE'] = pd.to_datetime(df_flight['FL_DATE']).dt.date
df_flight['DEP_TIME'] = pd.to_datetime(df_flight['DEP_TIME'], format='%H:%M').dt.time


# Combine the date and time columns into a single string with a space in between
datetime_str = df_flight['FL_DATE'].apply(str) + ' ' + df_flight['DEP_TIME'].apply(lambda x: x.strftime('%H:%M:%S') if not pd.isnull(x) else '01:08:24')

# Convert the resulting string to a Pandas timestamp
# Deduct 1 hr from departure time to create boarding time
timestamp_col = pd.to_datetime(datetime_str) - pd.Timedelta(hours=1)

# Add the new timestamp column to the DataFrame
df_flight['BOARDING_DATETIME']  = timestamp_col


# Convert timestamp to datetime object
df_weather['DATE'] = pd.to_datetime(df_weather['DATE'])
df_weather = df_weather.rename(columns={'Airport_Code': 'AIRPORT'})

df_origin = df_weather
df_origin = df_origin.add_prefix('ORIGIN_')
df_origin = df_origin.rename(columns={'ORIGIN_AIRPORT': 'ORIGIN', 'ORIGIN_DATE' : 'BOARDING_DATETIME'})

df_dest = df_weather
df_dest = df_dest.add_prefix('DEST_')
df_dest = df_dest.rename(columns={'DEST_AIRPORT': 'DEST', 'DEST_DATE' : 'BOARDING_DATETIME'})

# Sort DataFrame by date and time columns in ascending order
df_origin = df_origin.sort_values(by=['BOARDING_DATETIME'], ascending=True)
df_dest = df_dest.sort_values(by=['BOARDING_DATETIME'], ascending=True)
df_flight = df_flight.sort_values(by=['BOARDING_DATETIME'], ascending=True)

# Merge DataFrames based on time column and two additional columns within one-hour window
merged_df = pd.merge_asof(df_flight, df_origin, on='BOARDING_DATETIME', by=['ORIGIN'], tolerance=pd.Timedelta(minutes=61))
merged_df = pd.merge_asof(merged_df, df_dest, on='BOARDING_DATETIME', by=['DEST'], tolerance=pd.Timedelta(minutes=61))

print ("Merged df")
print (merged_df.columns)
print (merged_df.head(5))

merged_df.to_csv('C:\project_data\merged\merged_final.csv', index=False)