square=[]
start=1
for i in range(1,11):
    row=[i for i in range(start,start+10)]
    square.append(row)
    start+=10

for row in square:
    print(" ".join(map(str,row))))