import numpy as np 

arr_1=np.array([i for i in range(10)])
arr_2=np.array([i for i in range(10)])
print('-------------Array Creation-----------')
print()
print('arr_1 is ' , arr_1)
print('arr_2 is ', arr_2)
print()
#Addition
print('--------------Addition--------------')
print()
arr_sum=arr_1+arr_2
print("sum of arr_1 and arr_2 is : " , arr_sum)
print()
print('--------------Array Element Multiplication-------------')
print(arr_1*arr_2)
print()
print('-------------Dot Product-------------')
print(np.dot(arr_1,arr_2))
