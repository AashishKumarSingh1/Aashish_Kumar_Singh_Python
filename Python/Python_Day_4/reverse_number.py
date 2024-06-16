num = int(input("Enter the number : "))
rev=0
for i in range(1,num+1,1):
    rev=rev*10+num%10 
    num=num//10# // => this is used for integer division while this '/' is used for float division!
    if(num==0):
        break
else:
    print("Done")

print("The reverse of the number is : ",rev)