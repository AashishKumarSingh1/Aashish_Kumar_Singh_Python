def hcf_calculate(num1,num2):

    for i in range(2,max(num1,num2)+1):
        if num1%i==0 and num2%i==0:
            return i
    else:
        return 1

num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))

print(hcf_calculate(num1,num2))