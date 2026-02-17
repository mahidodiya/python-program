import pandas as pd 
df = pd.DataFrame({
    "City":["Surat","Surat","Mumbai","Mumbai","Delhi"],
    "Product":["Mobile","Laptop","Mobile","Laptop","Mobile"],
    "Sales":[20000,50000,22000,52000,21000]
})

print(pd.pivot_table(df,index="City",values="Sales",aggfunc="sum"))
print(pd.pivot_table(df,index="City",columns="Product",values="Sales",aggfunc="mean"))
print(pd.pivot_table(df,index="City",columns="Product",values="Sales",aggfunc=["mean","sum","max","min"]))
print(pd.pivot_table(df,index="City",columns="Product",values="Sales",fill_value=0))