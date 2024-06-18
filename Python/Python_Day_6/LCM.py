def LCMCalculator(num1,num2):
    for i in range(min(num1,num2),(num1*num2)+1):
        if(i%num1==0 and i%num2==0):
            return i
    else:
        print("Done!")
        return num1*num2

num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))
# print("LCM is : ",LCMCalculator(num1,num2))
LCM = LCMCalculator(num1,num2)
print("The LCM is : ",LCM)