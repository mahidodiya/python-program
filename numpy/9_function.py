import numpy as np
a=np.array([5,6,3])
b=np.array([10,20,30])
print(a,b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a + 5)
print(a * 2)
print('-'*10)
print(np.log(a))
print(np.exp(a))
print(np.sin(a))
print(np.cos(a))
print(np.cosh(a))
print(np.sqrt(a))

print('-'*50)
#aggrigate function
print("aggrigate function")
print('-'*50)
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
y = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x)
print(y)

#matrix multiplication
print(x @ y)
print(a.dot(b)) #same as above

z = np.array([10,20,30,100])
print(z)
print(z>20)
#aggrigate function 
print("Sum of all elements in z :",z.sum())
print("average of all elements in z :",z.mean())
print("minimum of all elements in z :",z.min())
print("maximum of all elements in z :",z.max())

#update
print("update")
print(z)
z[0]=11
print(z)
z[0:2]=[12,9]
print(z)