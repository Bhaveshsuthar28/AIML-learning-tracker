import pandas as pd

"""
    Missing Data Handling

    Type of Missing DaTa

    NaN(not a number)
    None(For object) 

    df.isnull()

    True -> NaN is Missing 

    False -> Value is Present
"""


data = {
    "Name": ["Ram", None, "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [28, 34, None, 30, 23, 40, 25, 32],
    "City": ["Delhi", "Mumbai", "Jaipur", "Ahmedabad", None, "Udaipur", "Indore", "Chandigarh"],
    "Salary": [50000, 60000, 45000, 52000, None, 70000, 48000, 58000],
    "Performance Score": [None, 90, 78, 92, 88, 95, 80, 89]
}


new_df = pd.DataFrame(data)


print(new_df)

print(new_df.isnull())

print(new_df.isnull().sum()) # no of missing value

"""
    How to Handle Missing data

    how to drop missing data(NaN and None) 
"""

# new_df.dropna(axis=0 , inplace=True) #axis=0 (rows) and axis=1 (columns)

# print(new_df)


"""
    Fill some Value where missing data

"""

# new_df.fillna(0 , inplace=True)

# print(new_df)

new_df["Name"].fillna("Bhavesh" , inplace=True)
new_df["City"].fillna("Delhi" , inplace=True)

new_df["Salary"].fillna(round(new_df["Salary"].mean()) , inplace=True)
new_df["Performance Score"].fillna(round(new_df["Performance Score"].mean()) , inplace=True)

new_df["Age"].fillna(round(new_df["Age"].mean()) , inplace=True) 

print(new_df)