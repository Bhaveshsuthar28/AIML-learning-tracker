import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [29, 22, 22, 30, 29, 29, 25, 25],
    "City": ["Delhi", "Mumbai", "Jaipur", "Ahmedabad", "Pune", "Udaipur", "Indore", "Chandigarh"],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}


new_df = pd.DataFrame(data)

"""
    Sorting Data Column sort_values()

    df.sort_values(by="Column_Name"(for rows remain empty) , ascendingTrue(for accending)/False , inplace=True)
"""

# new_df.sort_values(by="Age" , ascending=True , inplace=True)
new_df.sort_values(by=["Age" , "Salary"] , ascending=[True , True] , inplace=True)

print(new_df)

print(new_df["Age"].mean())
print(new_df["Age"].std())
print(new_df["Age"].var())
print(new_df["Age"].sum())
print(new_df["Age"].median())


groups = new_df.groupby("Age")["Salary"].mean().round()

print(groups)