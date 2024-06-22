# cook your dish here
t=int(input())
if t in range(1,201):
    for _ in range(t):
        n,x=map(int,input().split())
        if x>=1 and x<=n and n>=x and n<=20:
            print(n-x)