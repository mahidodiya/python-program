import pandas as pd
data={
    "Name":["joe","kai","liya"],
    "Age":[19,18,17],
    "Marks":[79,95,80]
}
df=pd.DataFrame(data)
print(df)
print(df["Age"])