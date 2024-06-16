num=int(input("Enter the number : "))

#function to square a number 
def square(num):
    return pow(num,2)


sqr_num=square(num)
new_num=sqr_num
sum=0
for i in range(1,len(str(sqr_num))+1):
    sum=sum+new_num%10
    new_num=new_num//10
    
print(sqr_num)
print(sum)
if(num==sum):
    print(f"This is a Neon Number!")
else:
    print(f"This is not a Neon Number!")