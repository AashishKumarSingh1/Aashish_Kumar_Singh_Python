def Sunny_Printer(num):
    x=pow(num+1,0.5)
    if(int(x)==x):
        return True
    else:
        return False

num=int(input("Enter the number : "))
print("The Sunny Number from 0 to ",{num}," are : ")
for i in range(0,num+1):
    if Sunny_Printer(i):
        print(i)
    else:
        pass
else:
    print("Done!")
