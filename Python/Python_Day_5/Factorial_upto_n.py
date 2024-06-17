num=int(input("Enter the number: "))

def factorial(num):
    #base condition
    if(num==1 or num==0 ):
        return 1
    else:
        return num*factorial(num-1)
    
for i in range(1,num+1):
    print("Factorial of ",i , " is " ,factorial(i))

else:
    print("Done1")
    