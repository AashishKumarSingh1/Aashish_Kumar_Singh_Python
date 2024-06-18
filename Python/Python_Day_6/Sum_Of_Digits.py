
num=int(input("Enter the number : "))
digit_sum=0

for i in range(0,len(str(num))):
    digit_sum +=num%10
    num//=10
else:
    print("Done!")
print(f"The sum of the digits is equal to : {digit_sum}")
