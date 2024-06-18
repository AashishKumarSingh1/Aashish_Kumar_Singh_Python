Triangle=[]
num=int(input("Enter the no. of rows of Floyd's Triangle: "))
current_number=1
for i in range (1,num+1):
    # row=[None for _ in range(1,i+1)]
    row=[]
    
    for j in range(0,i):
        row.append(current_number)
        current_number+=1
    Triangle.append(row)

print(Triangle)

for row in Triangle:
    print(str(row))

for row in Triangle:
    print(' '.join(map(str,row)))


