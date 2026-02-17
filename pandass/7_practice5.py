import pandas as pd
df=pd.DataFrame({
    "name":["bob","kity","tom","lara","peter"],
    "marks":[77,87,98,90,89]
},index=['a','b','c','d','e'])

print("loc-location based")
print(df.loc['b'])
print(df.loc['c',"marks"])

print("iloc-position based")
print(df.iloc[1])
print(df.iloc[2,0])
