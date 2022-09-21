# with open("weather_data.csv") as file:
#     body=file.readlines()
#     print(body)

import csv
import re



#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in file:
#         print(type(row))
#         temp_x = re.search(",(.+?),", row)
#         if temp_x.group(1) != 'temp':
#             temperature.append(temp_x.group(1))
#     print((temperature))


with open("weather_data.csv") as file:
    data = csv.reader(file)
    temperature = []
    for row in data:
        if row[1] != 'temp':
            print(row[1])
            temperature.append(row[1])

    print((temperature))

