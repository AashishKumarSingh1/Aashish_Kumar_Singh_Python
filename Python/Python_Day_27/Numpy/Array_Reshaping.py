import numpy as np 

arr_1=np.arange(9)
print('original array is : ',arr_1)
print()
#reshaping 
arr_reshape=arr_1.reshape((3,3))
print(arr_reshape)
print()
#Flattening 2d array
arr_flatten=arr_reshape.flatten()
print(arr_flatten)
