import pandas as pd
import numpy as np
data={
    "Name":["bob","joe","kity","koi","gigi"],
    "Age":[25,None,21,None,25],
    "Marks":[78,np.nan,91,70,85],
    "city":['london','paris','NYC','seoul','NYC']
}
df=pd.DataFrame(data)
print(df)
print('-'*50)

print("1.Handling Missing Values")
#isnull()-show boolean result of missing value
print(df.isnull())
print(df.isnull().sum())
#dropna()-remove row with missing value
print(df.dropna(how="all"))#onlf if all value is missing
print(df.dropna(subset=["Age"]))
#fillna()-insted of delete we fill mising value
print(df["Age"].fillna(20))
print(df["Marks"].fillna(df["Age"].mean(),inplace=True))
print("-"*50)

print("2.Sorting")
print(df.sort_values("Marks"))
print(df.sort_values("Marks",ascending=False))
print(df.sort_values(["city","Marks"]))

print("3.Grouping")
print(df.groupby("city")["Marks"].mean())
print(df.groupby("city")["Marks"].agg(["mean","max","min"]))

print("4.value count")
print(df["city"].value_counts())
print(df["city"].value_counts(normalize=True))

print("5.apply")
def grade(n):
    if n>=90:
        print("A+")
    elif n>=75:
        print("A")
    else:
        print("B")
    
df["Grade"]=df["Marks"].apply(grade)
print(df)