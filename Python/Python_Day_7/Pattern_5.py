

no_row=int(input("Enter the no. of row : "))
square=[]
for i in range (1,no_row+1):
    row=[i for i in range(5,0,-1)]
    square.append(row)

for row in square:
    print(" ".join(map(str,row)))
