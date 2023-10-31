import pandas
import csv

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     extra = []
#     for row in data:
#         temperatures.append(row[1])
#
#     temperatures.pop(0)
#     for row in temperatures:
#         extra.append(int(row))
#
#     temperatures = extra
#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"].mean())
#
# print(data[data["temp"] == data["temp"].max()])

# Primary Fur Color
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data["Primary Fur Color"].value_counts())