num = int(input("Enter the number: "))
ori_num=num
sum=0
for i in range(len(str(num)),0,-1):
    print(sum)
    sum=sum+pow(num%10,i)
    num=num//10
else:
    print("Done!")

print(sum)

if(ori_num==sum):
    print(f"{ori_num} is a Disarium Number!")

else:
    print(f"{ori_num} is not a Disarium Number!")
