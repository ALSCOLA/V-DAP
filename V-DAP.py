# Title: V-DAP
# Author: Anthony Scola, Emanuel Vargas
# Updated: 9/28/2020
# Version: 1.3.5

# Imports
from sys import platform
from sys import exit
from os import system
from time import sleep
import datetime
import random
import csv
import pandas as pd
import numpy

# definitions 
def clearScr(): # Clears screen on windows mac or linux
    if platform == "linux" or platform == "linux2":
        system('clear')  # For Linux/OS X
    elif platform == "darwin":
        system('clear')  # For Linux/OS X
    elif platform == "win32":
      system('cls')  # For Windows
    else:
        print('Unsupported platform error: ', platform) # Encountered an unknown platform
    return

def read2CSV(): # opens and reads the CSV Returns the data and legnth of the data
    with open('transportation_demand.csv') as g:
        csv_reader = csv.reader(g)
        data = list(csv_reader)
        dataLen = len(data)
    
    # Creates the data as a dataframe
    df = pd.read_csv('transportation_demand.csv', parse_dates=['DATE', 'TIME'])
        
    return data, dataLen, df

def avgTrend(data, dataLen, df): # [needs work] #averageQuarter-hourlyDemand.csv
    avg = df.groupby('TIME').mean().round(0).reset_index().sort_values(by=['TIME'])
    avg['TIME'] = pd.to_datetime(avg['TIME'])
    avg['DATE'] = df['DATE'].dt.date
    avg['TIME'] = df['TIME'].dt.time
    del avg['DATE']

    avg.to_csv('avgDemand.csv', index=False)
    return

def dailyTrend(data, dataLen, df): #dailyDemandTrend.csv
    daily = df['DEMAND'].groupby(df['DATE'].dt.to_period('D')).sum().reset_index()
    daily.to_csv('dailyDemand.csv', index=False)
    return

def statsReturn(data, dataLen, df): #statsReturn.csv
    header = ['Max Demand', 'Average Demand', 'Minimum Demand','Last updated'] # Can stay like this
    rows = [[str(df['DEMAND'].max()), str(df['DEMAND'].mean().round(0)), str(df['DEMAND'].min()), str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))]] # [needs to be programmed]
    wright2CSV('statsReturn',header,rows)
    return

def wright2CSV(filename,header,rows): # builds CSV [Complete]
    filename = filename + '.csv'
    with open(filename, 'wt') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(header) # write header
        csv_writer.writerows(rows) # write the rows
    return 

# Main
clearScr()
##print("Project has loaded\n") # Welcome msg
data, dataLen, df = read2CSV()

dailyTrend(data, dataLen, df)
avgTrend(data, dataLen, df)

statsReturn(data, dataLen, df)


#exit
print("\nWelcome to the V-DAP engine!\nV 0.2.9\n")
print("Please look through the following choices")
print("(1) Basic Predictive Analysis")
print("(2) Deep Learning Analysis")
print("(3) Stats")
print("(4) Settings\n")
exit()