import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "City": ["Delhi", "Mumbai", "Jaipur", "Ahmedabad", "Pune", "Udaipur", "Indore", "Chandigarh"],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}


new_df = pd.DataFrame(data)


"""
    Adding new Columns in existing dataFrames
"""


"""
    First Mathod
    Sqaure brackets df["Column_Name] = some_data
"""

print(new_df)

new_df["Bonus"] = new_df["Salary"]*0.1

print(new_df)

"""
    by using insert methods
    new_df.insert(loc=location of df , "Column_Name" , some_data)
"""

new_df.insert(0 , "Employe ID" , [10,20,30,40,50,60,70,80])

print(new_df)


"""
   Edit specfic value in dataFrame  
   df.loc[row_index , "Column_Name"] = new_Value
"""

new_df.loc[0 , "Salary"] = 60000

print(new_df)

new_df["Salary"] = new_df["Salary"] * 1.5

print(new_df)