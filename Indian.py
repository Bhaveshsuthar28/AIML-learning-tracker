import numpy as np
import pandas as pd

df = pd.read_csv("indian.csv")

print(f"\n\nMissing Value in CSV File\n\n{df.isnull().sum()}")

df.replace([np.inf , -np.inf] , np.nan , inplace=True)
 
df.replace()

df["Salary (INR)"].fillna(df["Salary (INR)"].mean() , inplace=True)

df["Age"].fillna(df)

print(f"\n\nMissing Value in CSV File\n\n{df.isnull().sum()}")

