# cook your dish here
t=int(input())
if t in range(1,101):
    for _ in range(t):
        x,a,b=map(int,input().split())
        if x in range(1,101) and ( a and b ) in range(0,101):
            if x > a*1+b*2 :
                print("NotQualify")
            else:
                print("Qualify")