import numpy as np

a=np.array([10,20,30,40,50])
b=np.array([11,22,30,44,55])
c=np.array([10,20,30,40,50])
d=np.array([[10,20,30,40,50]])
print(a,b,c,d)
#comparision
print("-->comparision")
print(a==b)
print(a==c)
print(np.all(a==b))
print(np.any(a==b))
#equal
print("-->equal()")
print(np.array_equal(a,c))
print(np.array_equal(b,c))
print(np.array_equal(a,d))
#logical opration
print("-->logical opration")
x=np.array([10,20,30])
y=np.array([10,40,30])
print(x,y)
result_and=np.logical_and(x<40,y<=30)
print("and-",result_and)
result_or=np.logical_or(x<40,y<=30)
print("or-",result_or)
result_not=np.logical_not(x>50)
print("not-",result_not)
result_xor=np.logical_xor(x<40,y<=30)
print("xor-",result_xor)

