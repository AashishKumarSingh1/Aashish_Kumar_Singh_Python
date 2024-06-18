

no_row=int(input("Enter the no. of row : "))
square=[]
start=1

for i in range(1,no_row+1):
    row=[i for i in range(start,(start+start*no_row)+1 ,+start)]
    square.append(row)
    start+=1
for row in square:
    print(" ".join(map(str,row)))