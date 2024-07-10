"""
Numpy First Code
"""
import numpy as np 
from time import time
start=time()
x=np.array([1,2,3,4,5])
end=time()
print(x,"Time : ",end-start,'start: ',start)
print(type(x))
print()
start=time()
y=[1,2,3,4,5]
end=time()
print(y,"time: ",end-start)
print(type(y))

#Numpy Array Creation 
# list1=[]
# for i in range(4):
#     list1.append(int(input("Enter : ")))

# array1=np.array(list1)
# print(array1)
# print(type(array1))

#Types of Array
#->1D array
array_1=np.array([1,2,3,4])
print(array_1)
print("Dimension of array_1 is : " , array_1.ndim)

#-> 2D Array
array_2=np.array([[2,3],[4,5]])
print(array_2)
print("Dimension of array_2 is : " ,array_2.ndim)

#-> 3D Array
array_3=np.array([[[3,4,5,6],[4,5,6,7]]])
print(array_3)
print(array_3.ndim)

#-> Creating N Dimensional Array
array_n=np.array([1,2,3,45],ndmin=5)
print(array_n)
print(array_n.ndim)

#Create Numpy Array using Function 
