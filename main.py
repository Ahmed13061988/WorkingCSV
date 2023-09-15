# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()
#
# print(data)

import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
data_list = data["temp"].tolist()
print(data_list)

average = data["temp"].mean()
print(average)

