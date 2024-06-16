def is_happy_number(num):
    seen_numbers = set()  # To keep track of numbers we've already seen to detect cycles
    ori_num = num
    
    while num != 1 and num not in seen_numbers:
        seen_numbers.add(num)
        sum_of_squares = 0
        while num > 0:
            digit = num % 10
            sum_of_squares += digit ** 2
            num //= 10
        num = sum_of_squares
    
    if num == 1:
        return f"The number {ori_num} is a Happy Number!"
    else:
        return f"The number {ori_num} is not a Happy Number!"

# Input from user
num = int(input("Enter the number:"))
happyNum=is_happy_number(num)

if(happyNum):
    print(f"The {num} is a Happy Number!")

else:
    print(f"The {num} is not a Happy Number!")
          

# num=int(input("Enter the number : "))
# ori_num=num
# sum=10
# while sum>9:
#     for i in range (1,len(str(sum))+1):
#         if(i==1):
#             sum=0
#         sum=pow(num%10,2)+sum
#         num=num//10
# print(num)
# print(sum)
# if(sum==1):
#     print(f"The {ori_num} is a Happy Number!")

# else:
#     print(f"The {ori_num} is not a Happy Number!")
