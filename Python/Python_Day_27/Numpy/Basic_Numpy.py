#numpy object name-> ndarray object
import numpy as np 

arr=np.array([1,2,3,4,5])
print(arr)

#To check version details of package 

print('version: ',np.__version__)
print()
#Creating Array

a1=np.array([1,2,3])
a2=np.array(([1,2,3]))
a3=np.array([12,34,56],ndmin=5)
print(a1,a1.ndim)
print(a2,a2.ndim)
print(a3,a3.ndim)
print()
print(type(a3))