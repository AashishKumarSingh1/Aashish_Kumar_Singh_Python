import numpy as np

arr_1=np.array([i for i in range(10)])

print("Array is : ",arr_1,',Dimension is : ', arr_1.ndim, ",Type is : ",type(arr_1))
print()
# 2* 2 array -> 
arr_2=np.zeros((2,5))
print("Array is : ",arr_2,',Dimension is : ', arr_2.ndim, ",Type is : ",type(arr_2))
print()
#3*3 array->
arr_3=np.ones((3,5))
print("Array is : ",arr_3,',Dimension is : ', arr_3.ndim, ",Type is : ",type(arr_3))
print()