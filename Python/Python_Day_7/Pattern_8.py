

no_row=int(input("Enter the no. of row : "))
square=[]
start=2
for i in range(1,no_row+1):
    row=[j for j in range(start,start+9,+2)]
    start+=10
    square.append(row)
else:
    print("Done!")
for row in square:
    print(" ".join(map(str,row)))