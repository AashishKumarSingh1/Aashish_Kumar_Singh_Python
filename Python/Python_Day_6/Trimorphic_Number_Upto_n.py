def is_Trimorphic(num):
    return str(pow(num,3)).endswith(str(num))

num=int(input("Enter the upper limit number : "))
print(f"Trimorphic Number Upto {num} are : ")
for i in range(1,num+1):
    if is_Trimorphic(i):
        print(i)
else:
    print("Done!")