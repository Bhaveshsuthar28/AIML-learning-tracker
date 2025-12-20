import pandas as pd
"""
    pd.merge(df1 , df2 , on="Column_Name" , how="type of join")
"""

df_customers = pd.DataFrame({
    "CustomerID" : [1,2,3,5],
    "Name" : ["Ramesh" , "Suresh" , "Bhavesh" , "Rajesh"]
})

df_orders = pd.DataFrame({
    "CustomerID" : [1,2,3,4],
    "OrderAmount" : [250 , 342 , 2432 , 100]
})

new_df1 = pd.merge(df_customers , df_orders , on="CustomerID" , how="inner")
new_df5 = pd.merge(df_customers , df_orders , on="CustomerID" , how="outer")

print(new_df1)
print(new_df5) 