def digit_sum(num):
    sum=0
    for i in range(1,num+1):
        sum+=num%10
        num=num//10
    return sum

num=int(input("Enter the number : "))
digitSum=digit_sum(num)
result_digitSum=digit_sum(digitSum)
print(f"The Super Digit of the {num} is : {result_digitSum}")