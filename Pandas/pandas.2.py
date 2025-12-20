import pandas as pd

"""
    1.Understand the Data set
    2.Identify the problems
    3.plan next steps
"""

#.head() display first 5 rows
#.tail() display last 5 rows


#.head(n) display first n rows
#.tail(n) display last n rows

df = pd.read_csv("indian.csv")

print(df.head())
print(df.head(15))

print(df.tail())
print(df.tail(10))


"""
    in your data you don't know 

    1-> column , rows?
    2-> what type of?
    3-> missing data

    so we use .info() method


    1-> number of rows and column 
    2-> column name 
    3-> int64 float64 object
    4-> non null counts
    5-> memory usage of the data frame
"""

print("Display info of data Frame of indian.csv\n" , df.info())

#output of these code

"""
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 100 entries, 0 to 99
    Data columns (total 8 columns):
    #   Column              Non-Null Count  Dtype  
    ---  ------              --------------  -----  
    0   Employee ID         100 non-null    int64  
    1   Name                100 non-null    object 
    2   Age                 96 non-null     float64
    3   Salary (INR)        100 non-null    float64
    4   Experience (Years)  100 non-null    int64  
    5   City                97 non-null     object 
    6   Department          100 non-null    object
    7   Performance Rating  100 non-null    float64
    dtypes: float64(3), int64(2), object(3)
    memory usage: 6.4+ KB
    Display info of data Frame of indian.csv
    None
"""



#Summary of numeric Data of column

print("Summary of Numeric Column\n",df.describe())


data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age": [28, 34, 22, 30, 29, 40, 25, 32],
    "City": ["Delhi", "Mumbai", "Jaipur", "Ahmedabad", "Pune", "Udaipur", "Indore", "Chandigarh"],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance Score": [85, 90, 78, 92, 88, 95, 80, 89]
}


new_df = pd.DataFrame(data)

print(f"Simple dataframe\n{new_df}")

print(f"Info of these DataFrame\n{new_df.info()}\n\nDiscription of Numeric Column\n{new_df.describe()}")
 