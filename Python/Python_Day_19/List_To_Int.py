list_list=[2,2,3,4,5]
int_list=map(str,list_list)
print(int_list)
print(tuple(int_list))
int_list=' '.join(map(str,list_list))
print(int_list)

#list to int 
list_1=[1,2,3,4,5]
list_1=list(map(str,list_1))
str_1=''.join(list_1)
int_1=int(str_1)
print("num is : ", int_1 , " and type is : ",type(int_1))


