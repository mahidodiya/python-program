import numpy as np
#genrates float random value
print(np.random.rand(5))
#gentares integer
print(np.random.randint(10,30,size=6))
#Randomly selects elements from a given list or array
print(np.random.choice([10,33,66,22,11,54],size=3))
print(np.random.choice([0,1,2],size=6,p=[0.5,0.3,0.2]))
#Shuffles array
arr=np.array([11,43,66,78,22])
np.random.shuffle(arr)
print(arr)
#Returns a shuffled copy of the array
np.random.permutation(arr)
print(arr)
#Generates random float values within a specified range
print(np.random.uniform(5,10,size=5))
#Simulates binomial distribution (success/failure)
print(np.random.binomial(n=5,p=0.5,size=5))