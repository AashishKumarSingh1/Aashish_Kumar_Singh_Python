import numpy as np 

arr_3=np.array([i for i in range(10)],ndmin=3)

print(arr_3)
print()

#extracting third element
print('third element is :' , arr_3[0,0,2])

#extracting a subarray from above array 

print('One Subarray is : ' , arr_3[0,0,2::3])