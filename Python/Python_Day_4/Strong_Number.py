num=int(input("Enter the number : "))
ori_num=num
# function to find the factorial of any number
def factorial(num):
    # i am using recursion 
    #base condition

    if(num==1 or num==0):
        return 1
    
    return num*factorial(num-1)

sum=0
for i in range(1,len(str(num))+1):
    sum=sum+factorial(num%10)
    num=num//10

if(sum==ori_num):
    print(f"This number is a Strong Number!")
else:
    print(f"The number is not a Strong Number!")


    
