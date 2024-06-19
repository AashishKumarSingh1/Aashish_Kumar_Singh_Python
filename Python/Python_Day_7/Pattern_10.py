no_row=int(input("Enter the no. of row : "))
square=[]

for i in range(1,no_row+1):
    row=[]
    ini=1
    for j in range(1,no_row+1):
        if j%2!=0:
            row.append(ini)
            ini+=1
        else:
            if i>=2:
                if i==(no_row-1) and j==2:
                    row.append(2)

                else:
                    
                    row.append(square[i-2][j-1])
                    
            else:
                row.append(1)
    square.append(row)
else:
    print("Done!")
for row in square:
    print( " ".join(map(str,row)))
