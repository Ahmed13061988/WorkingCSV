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

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# data_list = data["temp"].tolist()
# # print(data_list)
#
# average = data["temp"].mean()
# max_temp = data["temp"].max()
# # print(data[data.temp == max_temp])
#
# monday = data[data.day == "Monday"]
# temp_in_f = (monday.temp * 1.8) + 32
# print(temp_in_f)

data_dict = {
    "students": ["Amy", "James", "Ahmed"],
    "scores": [76, 56, 90]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_csv_file")

