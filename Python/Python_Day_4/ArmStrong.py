num=str(input("Enter the number : "))
count=len(num)
num=int(num)
ori_num=num
sum=0
# print(len(num)) => not valid as num is a integer and len function is not defined for an integer value!
for i in range(1,count+1):
    sum=pow(num%10,3)+sum
    num=num//10 # remember to add // for integer division othewise answer becomes somewhat different!
    # if(num==0):
    #     break
else:
    print("Done")
if (sum==ori_num):
    print(f"This is an armstrong number!")

else:
    print(f"This is not a armstrong number!")
