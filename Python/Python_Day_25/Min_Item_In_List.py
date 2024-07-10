from functools import reduce

def func(list_1:list):
    min_val=list_1[0]
    min_find=lambda min_val,y:min_val if min_val<y else y

    return reduce(min_find,list_1)

list_1=[7,12,9,4,11]
min_val=func(list_1)
print(min_val)
