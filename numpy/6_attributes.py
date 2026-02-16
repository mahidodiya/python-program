import numpy as np
arr1=np.array([[1,2.,3],[4,5,6]])
print("array1:")
print(arr1)
arr2=np.array([[[1,2,3],[4,5,6]],[[11,12,13],[14,15,16]]])
print("array2:")
print(arr2)
#1.dimetion
print("dimention of array1:",arr1.ndim)
print("dimention of array2:",arr2.ndim)
#2.shape(no of rowxcolumns)
print("shape of array1:",arr1.shape)
print("shape of array2:",arr2.shape)
#3.size(no of element)
print("size of array1:",arr1.size)
print("size of array2:",arr2.size)
#4.data type
print("datatype of array1:",arr1.dtype)
print("datatype of array2:",arr2.dtype)
#5.itemsize(space occupied by array-->byte per element)
print("per element space occupied by array1:",arr1.itemsize)
print("per element space occupied by array2:",arr2.itemsize)
#6.nbytes(sizexitemsize-->total memory occupaied by array)
print("total space occupied by array1:",arr1.nbytes)
print("total space occupied by array2:",arr2.nbytes)
#7.transport(convert row into column)
print("transport of array1:",arr1.T)
print("transport of array2:",arr2.T)
#array.data-->(gives direct access to the memory location where the NumPy array is stored)
print("location:",arr1.data)
print("location:",arr2.data)
#array.flags-->(gives information about how a NumPy array is stored in memory and what operations are allowed on it)
print("flag:",arr1.flags)
b=arr1[1:3]
print("flag:",b.flags)


#complex array
print("complex number!!")
arr3=np.array([[2+4j],[2+3j]])
print("array")
print(arr3)
print("dimention:",arr3.ndim)
print("real part:",arr3.real)
print("imegenary part",arr3.imag)

#copy() method
print("copy method")
a=np.copy(b)
print(a)
list=[2,3,4,5,6,7]
x=np.copy(list)
print(x)

