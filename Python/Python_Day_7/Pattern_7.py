

no_row=int(input("Enter the no. of row : "))
square=[]
start=1
for i in range(1,no_row+1):
    row=[j for j in range(start,start+9,+2)]
    square.append(row)
    start+=10
for row in square:
    print(" ".join(map(str,row)))
