import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
c_black = 0
c_cinnamon = 0
c_gray = 0


black_sq=len(data[data["Primary Fur Color"] == "Black"])
print(black_sq)

gray_sq=len(data[data["Primary Fur Color"] == "Gray"])
print(gray_sq)

data_dict = {
    "Fur Color": ["Black", "Gray"],
    "Count": [black_sq, gray_sq]
}

df = pandas.DataFrame(data_dict)
df.to_csv("final_extracted_data")

print(data_dict)

