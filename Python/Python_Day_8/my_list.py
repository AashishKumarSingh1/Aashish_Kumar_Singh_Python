list=["Hello","Aashish","Kumar","Singh"]
print(list)
print(" ".join(list))
print("*".join(map(str,list)))

for items in list:
    print(items)
print(list[0]+list[1])

#Access items - index range 

print(list[2:5])
print(list[0:2])

#Access items negative index range 

print(list[-1])
print(list[-5:-2])

#Modify item

list[0]="Namaste"
for item in list: 
    print(item)

#length of list 
print(len(list))

##method : append(),insert(),remove(),pop(),def(),clear(),
#search = input("Enter the name/list / or anything")
#if search in list:
#listB=list.copy()
#listB=list(list)
#list=listA+listB
#list.reverse()
#my_list.count('Hello')
#list.sort(reverse==True)
#sort list(according to criteria )
#def findLen(e): return len(e)
#list.sort(key=findLen)