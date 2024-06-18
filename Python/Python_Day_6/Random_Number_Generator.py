import random
# list_number = [i for i in range(1, 11) for _ in range(10)]
list_number = [i for i in range(1, 11) ]
computer_select=random.choice(list_number)
print(f"The computer selects : {computer_select}")

#modified random generator 

min=int(input("Enter the minimum number : "))
max=int(input("Enter the maximum number : "))

list_number=[i for i in range(min,max+1)]
computer_select=random.choice(list_number)
print(f"The computer selects : {computer_select}")