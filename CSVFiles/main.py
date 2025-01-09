# with open("100_Days_Bootcamp\CSVFiles\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("100_Days_Bootcamp\CSVFiles\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row != "temp":
#             temperatures.append(int(row[1]))

#     print(temperatures)

# data = pandas.read_csv("100_Days_Bootcamp\CSVFiles\weather_data.csv")
# print(data["temp"])

# temp_list = data["temp"].to_list()

# print(data["temp"].max())

# print(data[data.temp > 20])

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")


import pandas
data = pandas.read_csv("100_Days_Bootcamp\CSVFiles\CentralParkData.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("100_Days_Bootcamp\CSVFiles\squirrel_count.csv")