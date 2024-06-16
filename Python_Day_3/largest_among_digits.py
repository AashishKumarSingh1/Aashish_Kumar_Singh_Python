#This program is going to show the largest among the provided numbers!
count=int(input("Enter how many numbers you want to provide: "))
max=0
min=0
for i in range(1,count+1):
    n1=int(input("Enter the number : "))
    if(i==1):
        max=n1
        min=n1
    else:
        if(max<n1):
            max=n1
        else:
            if(min<n1):
                pass
            else:
                min=n1
        

print("The maximum value among all is : ",max, " and the minimum value among all the numbers is : ",min)
