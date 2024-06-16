#This program is going to print the fibonacci series 
#The series looks like : 1,1,2,3,5,8

previous = 1
preprevious=1
count=int(input("Enter how many fibonacci series you want: "))
print("The fibonacci series is =>")
for i in range(1,count+1):
    if(i==1 or i==2):
        print("1")

    else:
        n1=previous+preprevious
        print(n1)
        preprevious=previous
        previous=n1


        