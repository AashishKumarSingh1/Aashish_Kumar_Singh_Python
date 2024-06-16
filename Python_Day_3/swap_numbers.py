#This program is going to swap two numbers!

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
print("n1 is taken reference for the first number and n2 is taken the reference for the second number!")
print("Befor swapping n1 is : ",n1 , " and n2 is : ",n2)

n1 = n1+n2
n2=n1-n2
n1=n1-n2

print("After swapping n1 is : ",n1 , " and n2 is : ",n2)