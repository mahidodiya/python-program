import pandas as pd
data={
    "Name":['kitty','emily','conrad','belly','jerimhaya'],
    "Age":[20,31,28,22,27],
    "Marks":[88,67,85,99,80],
    "city":['paris','nyc','busan','seoul','londan']
}
df=pd.DataFrame(data)
print(df)
print("-"*50)

#Selecting Columns
print(df['Name'])
print(df[['Name','Age']])
print(df[['Name','Age','city']])
print(df.iloc[1:,2])
print("-"*50)

#filtering
print(df[df['Marks']>80])
print(df[(df["Marks"]>=80)&(df['Age']>25)])
print("-"*50)
#Adding Column
df["grade"]=['A','B+','A','A+','A']
print(df)
df["Age_after_5years"]=df["Age"]+5
print(df)
print("-"*50)
#Deleting Columns
df.drop("grade",axis=1,inplace=True)
print(df)
