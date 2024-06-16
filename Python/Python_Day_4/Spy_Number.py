num = int(input("Enter the number : "))
sum=0 
multiple=1
ori_num=num

for i in range(1,len(str(num))+1):
    sum+=num%10
    multiple*=num%10
    num=num//10
print(sum,multiple)
if(multiple==sum):
    print(f"The {ori_num} is a Spy Number!")

else:
    print(f"The {ori_num} is not a Spy Number!")