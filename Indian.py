import pandas as pd
import numpy as np

df = pd.read_csv("indian.csv")

df.replace((np.inf , -np.inf) , np.nan , inplace=True)

df["Age"].fillna(round(df["Age"].mean()) , inplace=True)

df["Salary (INR)"].fillna(round(df["Salary (INR)"].mean()) , inplace=True)

df["Experience (Years)"].fillna(round(df["Experience (Years)"].mean()) , inplace=True)

df["City"].fillna("Jodhpur" , inplace=True)

df["Performance Rating"].fillna(df["Performance Rating"].median() , inplace=True)

df.drop_duplicates(inplace=True)

df["Age"] = np.where(df["Age"] < 0 , round(df["Age"].mean()) , df["Age"])

df["Performance Rating"] = np.where(df["Performance Rating"] < 0 , df["Performance Rating"].mean() , df["Performance Rating"])

df["Salary (INR)"] = np.where(df["Salary (INR)"] < 0 , round(df["Salary (INR)"].mean()) , df["Salary (INR)"])

df["Experience (Years)"] = np.where(df["Experience (Years)"] < 0 , round(df["Experience (Years)"].mean()) , df["Experience (Years)"])

salary_mean = df["Salary (INR)"].mean()
salary_std = df["Salary (INR)"].std()
lower = salary_mean - (3*salary_std)
upper = salary_mean + (3*salary_std)

df = df[(df["Salary (INR)"] >= lower) & (df["Salary (INR)"] <= upper)]

df.to_csv("Indian_employe.csv" , index=False)

print("Indian_employe.csv created successFully")