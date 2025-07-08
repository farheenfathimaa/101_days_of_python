# without CSV
# with open("weather_data.csv") as weather_data:
#     data= weather_data.readlines()
#     print(data)

# without pandas
# import csv
# with open('weather_data.csv') as weather_data:
#     data=csv.reader(weather_data)
#     temperatures=[]
#     for row in data:
#         if row[1]!= "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#     for row in data:
#         print(row)

# with pandas
import pandas as pd
# data=pd.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict=data.to_dict()
# print(data_dict)

# temp_list=data["temp"].to_list()
# print(temp_list)
# total_temp=0
# for temp in temp_list:
#     total_temp+=temp

# # sum() can be used for adding column/series values
# print(f"average temperature: {total_temp/len(temp_list):.2f}")

# print(data["temp"].mean())
# print(data["temp"].max())

# get the row values
# print(data[data.temp==data.temp.max()])

# monday's temp from C to F
# monday=data[data.day=="Monday"]
# cTemp = monday.temp[0]
# fTemp=(cTemp*9/5)+32
# print(fTemp)

#create a dataframe from scratch
# data_dict={
#     "students":["amy","john","angela"],
#     "scores":[87,64,92]
# }
# data=pd.DataFrame(data_dict)
# print(data)

# data.to_csv("new_data.csv")



#squirrel census data
data=pd.read_csv("squirrel_data.csv")
gray_squirrels_count=len(data[data["Primary Fur Color"]== "Gray"])
cinnamon_squirrels_count=len(data[data["Primary Fur Color"]== "Cinnamon"])
black_squirrels_count=len(data[data["Primary Fur Color"]== "Black"])
data_dict={
    "Fur Color":["Gray", "Cinnamon","Black"],
    "Count":[gray_squirrels_count,cinnamon_squirrels_count,black_squirrels_count]
}
squirrel_count=pd.DataFrame(data_dict)
squirrel_count.to_csv("squirrel_count.csv")