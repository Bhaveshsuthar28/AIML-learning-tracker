import pandas as pd

#tread data from csv file into a dataframe

df = pd.read_csv("indian.csv" , encoding="utf-8")

print(df)

#if your data on cloud so you can read your data by a libary name is gcsfs

data = {
    "Name" : ["Ram" , "Shyam" , "Bhavesh"],
    "Age" : [10,20,30],
    "City" : ["Bhopal" , "Mumbai" , "Dehli"]
}

new_df = pd.DataFrame(data)

new_df.to_csv("city_data.csv" , index=False)

print(new_df)