import pandas as pd

"""
    1-> How big is your data
    2-> What are the names of coloumn

    shape(attribute which give you no of rows and columns) and columns(name of all columns)
"""

data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "City": ["Delhi", "Mumbai", "Jaipur", "Ahmedabad", "Pune", "Udaipur", "Indore", "Chandigarh"],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}


new_df = pd.DataFrame(data)

print(f"Shapes of data frame {new_df.shape}\n\n")
print(f"Name of All Columns of data frame {new_df.columns}")



"""
    1-> How to select a specific column
    2-> How to filter rows and columns
    3-> How to combine multiple conditions
"""

"""
selecting a columns 

column = new_df["Column Name"]

subset = new_df[["Column1"] , ["Column2"] , ["..."]]

filtering rows
by help of boolean indexing

fiteredRows = df[df["Column Name] > conditions]

"""

Columns = new_df["Name"]

print(Columns)

subset_new_df = new_df[["Name" ,"Salary"]]

print(subset_new_df)


Filter_new_df_Salary = new_df[(new_df["Salary"] > 52000) & (new_df["Salary"] < 65000)]

print(Filter_new_df_Salary)