import pandas
#import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             print(row[1])
#             temperature.append(int(row[1]))
#
#     print((temperature))


data=pandas.read_csv("weather_data.csv")
# print(data)

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()

mon=data[data.day == "Monday"]
print(mon)
m_temp =9/5 *(int(mon.temp)) +32
print(f"{m_temp} F")



# create dataframe from scratch
data=pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")