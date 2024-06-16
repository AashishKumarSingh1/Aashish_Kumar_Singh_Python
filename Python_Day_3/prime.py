print("This program is going to check whether a number is prime or not!")
n1=int(input("Enter the number : "))
# i=1
# for i in range(2,n1):
#     n1=i
#     break

# print(n1)
is_prime=True
for i in range(2,n1):
    if n1%i==0:
        is_prime=False
        break

print("The Number is a prime number : ",is_prime)