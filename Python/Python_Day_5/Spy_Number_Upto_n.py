def spy_Printer(num):
    sum_digits = 0
    product_digits = 1
    ori_num = num

    for i in range(1,len(str(num))+1):
        digit = num % 10
        sum_digits += digit
        product_digits *= digit
        num = num // 10

    return sum_digits == product_digits

num = int(input("Enter the number: "))

for i in range(1, num + 1):
    if spy_Printer(i):
        print(f"The number {i} is a Spy Number!")
