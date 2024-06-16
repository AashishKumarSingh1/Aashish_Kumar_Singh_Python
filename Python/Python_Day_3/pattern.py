# row = int(input("Enter how many row you want to print: "))



# for j in range(3,0,-1):#with this we are using range in reverse order from 3 to 0 with the exclusion of 0
#     print("#")
#     j-=1

# for i in range(1,row):
#     print("*")
#     i+=1



row = int(input("Enter how many rows you want to print: "))

# Loop to print '#' in decreasing order
for j in range(3, 0, -1):
    print("#" * j)

# Loop to print '*' in increasing order based on user input
for i in range(1, row + 1):
    print("*" * i)


row = int(input("Enter how many rows you want to print: "))

# Loop to print both '#' and '*' in alternating lines
for i in range(3, 0, -1):
    print("#" * i + "*" * (row - i))

