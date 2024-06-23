# cook your dish here
t=int(input())
if t in range(1,5001):
    for _ in range(t):
        n,x=map(int,input().split())
        if n>=2 and n<=100 and x>=0 and x<=n:
            final_side=min(n-x,x)
            
            print(final_side)