# cook your dish here
t=int(input())
if t in range(1,1001):
    for _ in range(t):
        n,x=map(int,input().split())
        if (n and x ) in range(1,101):
            if n<x:
                print("0")
            elif int(n-x)/4 !=(n-x)//4:
                print((n-x)//4 + 1)
            else:
                print((n-x)//4)