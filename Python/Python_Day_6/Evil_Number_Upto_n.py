def is_Evil(num):
    list=[]
    while num!=0:
        list.append(num%2)
        num//=2
        

    if ( list.count(1)%2==0):
        return True
    else:
        return False


num=int(input("Enter the upper limit number : "))
print(f"The Evil number from 1 to {num} are: ")
for i in range(1,num+1):
    if is_Evil(i):
        print(i)
else:
    print("Done!")
