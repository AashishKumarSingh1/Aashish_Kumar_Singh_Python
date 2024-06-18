

num=int(input("Enter the number : "))

# for i in range(len(str(num)),-1,-1):
#     print(num[i])
# else:
#     print("Done!")
rev=0
for i in range(1,len(str(num))+1):
    rev=rev*10+num%10
    num=num//10

print(rev)

