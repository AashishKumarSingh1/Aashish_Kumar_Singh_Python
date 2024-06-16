count= input("how many numbers you want to enter : ")
count=int(count)
max=0
while count>0:
    number=input("Enter the number : ")
    number=int(number)
    if(max<=number):
        max=number
    else:
        pass
    count-=1

print("Among all these numbers the max is  : " , max)