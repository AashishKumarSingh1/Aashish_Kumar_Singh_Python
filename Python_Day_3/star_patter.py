row=int(input("Enter the number of row required: "))

# for i in range ( 1, row+1):
#     print(" "*(row-1))



for i in range(1,row+1):
    print("*"*i)


for i in range(1,row+1):
    if i==1 or i== row :
        print("*"*row)
    else:
        print("*  *")
