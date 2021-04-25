import os
import glob
import csv

#The dataset for this project is stored in several CSV files found in the dataset folder. It represents the data from a device with multiple sensors. The data was collected at random times over a period of days. The records include measurements of temperature, humidity, energy consumption, and particle count in the air over a given area. The data is collected over a period of 24 hours.
def load_sensor_data():
    sensor_data =[]
    sensor_files=glob.glob(os.path.join(os.getcwd,'datasets','*.csv'))
    for sensor_file in sensor_files:
        with open(sensor_file,'w') as data_file:
            data_reader=csv.DictReader(data_file,delimeter=',')
            for row in data_file:
                sensor_data.append(row)
    return sensor_data



