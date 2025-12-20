"""
Docstring for Pandas.pandas.6
"""

import pandas as pd

"""
    Fill missing Data

    1-> Preserve data intergrity
    2-> smooth trends
    3-> avoid data loss

    interpolate()
"""

data = {
    "Name": ["Ram", "Bhavesh", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [28, 34, None, 30, 23, 40, 25, 32],
    "City": ["Delhi", "Mumbai", "Jaipur", "Ahmedabad", "Jodhpur", "Udaipur", "Indore", "Chandigarh"],
    "Salary": [50000, 60000, 45000, 52000, None, 70000, 48000, 58000],
    "Performance Score": [None, 90, 78, 92, 88, 95, 80, 89]
}


new_df = pd.DataFrame(data)


new_df.interpolate(method="linear" , inplace=True) #linear , polynomial , line


print(new_df)