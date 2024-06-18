def is_Pronic(num):
    for i in range(1,num):
        if(i*(i+1)==num):
            return True
    else:
        return False

num=int(input("Enter the upper limit: "))
print(f"Pronic Number upto {num} are: ")
for i in range(1,num+1):
    if is_Pronic(i):
        print(i)
else:
    print("Done!")
