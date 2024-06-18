def is_Disarium(num):
    ori_num=num
    sum=0
    for i in range(len(str(num)),0,-1):
        sum=sum+pow(num%10,i)
        num=num//10
    if(sum==ori_num):
        return True
    else:
        return False


number=int(input("Enter the upper limit number : "))

for i in range ( 1, number+1):
    if is_Disarium(i):
        print(f"The {i} is a Disarium Number!")

else:
    print("Done")