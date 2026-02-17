import pandas as pd
import numpy as np
student=pd.DataFrame({
    'id':[1,2,3,4,5],
    'name':['aena','juliya','gen','cooku',None]
})
marks=pd.DataFrame({
    'id':[1,2,3,4,5],
    'marks':[75,70,88,90,np.nan]
})

#join
#merge(inner join)
print(pd.merge(student,marks,on="id"))
#left join
print(pd.merge(student,marks,on="id",how="left"))