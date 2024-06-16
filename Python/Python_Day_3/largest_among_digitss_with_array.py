#This program is going to show maximum and minimum value using the method max() and min() used in list data type
list=[]
count=int(input("Enter how many numbers you want to enter: "))
for i in range(count):
    n1=int(input("Enter the number: "))
    list.append(n1)

print("The max is : ",max(list))
print("The min is : ",min(list))