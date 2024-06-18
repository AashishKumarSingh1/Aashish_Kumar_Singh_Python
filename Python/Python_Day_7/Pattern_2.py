

no_row=int(input("Enter the no. of row : "))
square=[]
for i in range(1,no_row+1):
    row=[]
    for j in range(1,no_row+1):
        row.append(i)
    square.append(row)
else:
    print("Done!")
# print(square)
for row in square:
    row_pattern = " ".join(map(str,row))
    print(row_pattern)

