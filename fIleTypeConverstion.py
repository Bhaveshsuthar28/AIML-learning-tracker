import pandas as pd

df = pd.read_csv("indian.csv")

df.to_excel("indian.xlsx" , index=False)

print("excel file created successfully")