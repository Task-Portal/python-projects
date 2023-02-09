import pandas

# data = pandas.read_csv("weather-data.csv")
#
# max_n = data["temp"].max()
# # print(data[data.temp == max_n])
#
# monday= data[data.day=="Monday"]
# monday_temp = int(monday.temp)*9/5+32
# print(monday_temp)

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

colors = data["Primary Fur Color"].dropna().unique()
gray = data[data["Primary Fur Color"] == "Gray"]
gray_count = gray["Primary Fur Color"].count()
black = data[data["Primary Fur Color"] == "Black"]
black_count = black["Primary Fur Color"].count()
cin = data[data["Primary Fur Color"] == "Cinnamon"]
cin_count = cin["Primary Fur Color"].count()

s_dict = {
    "Fur Color": colors,
    "count": [gray_count, cin_count, black_count]
}

data_n = pandas.DataFrame(s_dict)
data_n.to_csv("Calculations")
print(data_n)
