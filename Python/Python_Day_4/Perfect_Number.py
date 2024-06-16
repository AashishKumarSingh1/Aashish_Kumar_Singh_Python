num= int(input("Enter the number : "))
f_l_t_n=[]
sum=0
#function to derive the factors of a number 
def factor_less_than_num(num):
    sum=0
    for i in range(1,num+1):
        if num%i==0:
            if i<num:
                sum=sum+i
                f_l_t_n.append(i)
    else:
        print("Done!")
        # print(sum)

    return sum

#function to check perfect number 
 
def perfectNum(num,sum):
    if(num==sum):
        print(f"The {num} is a perfect number!")
    else:
        print(f"The {num} is not a perfect number!")
    return 0

sum=factor_less_than_num(num)
perfectNum(num,sum)


