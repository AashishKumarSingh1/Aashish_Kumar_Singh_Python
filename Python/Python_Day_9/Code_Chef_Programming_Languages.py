t=int(input())
if t in range(1,289):
    for i in range(t):
        a,b,a1,b1,a2,b2=map(int,input().split())
        if a in range(1,5) and b in range(1,5) and a1 in range(1,5) and b1 in range(1,5) and a2 in range(1,5) and b2 in range(1,5) and a!=b and a1!=b1 and a2!=b2:
            #input -> 1 2 2 1 3 4 :: output -> 1
            if ((a,b) == (a1,b1)) or ((a,b) == (b1,a1)):
                print("1")
            elif ((a,b)==(a2,b2)) or ((a,b) == (b2,a2)):
                print("2")
            else:
                print("0")
else:
    pass
