
# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()
#
# print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)

