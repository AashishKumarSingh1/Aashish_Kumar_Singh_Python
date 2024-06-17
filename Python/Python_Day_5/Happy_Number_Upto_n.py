def Happy_Printer(num):
    seen_numbers = set()
    
    while num != 1 and num not in seen_numbers:
        seen_numbers.add(num)
        sum_of_squares = 0
        for i in range(1,len(str(num))+1):
            digit = num % 10
            sum_of_squares += digit ** 2
            num //= 10
        num = sum_of_squares
    
    return num == 1

num = int(input("Enter the number: "))
for i in range(1, num + 1):
    if Happy_Printer(i):
        print(i)
print("Task Completed!")
