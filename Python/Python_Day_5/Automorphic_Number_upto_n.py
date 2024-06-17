def Automorphic_Printer(num):
    is_auto=str(pow(num,2)).endswith(str(num))
    return is_auto

number=int(input("Enter the number : "))
print("The Automorphic Number from 1 to ",number ,"are :")
for i in range(1,number+1):
    is_auto=Automorphic_Printer(i)
    if(is_auto):
        print(i," : ",pow(i,2))
    else:
        pass

else:
    print("Done!")

