

no_row=int(input("Enter the no. of row : "))
square=[]
for i in range(no_row,0,-1):
    row=[]
    for j in range(1,no_row+1):
        row.append(i)
    square.append(row)
else:
    print("Done!")

for row in square:
    print(" ".join(map(str,row)))

