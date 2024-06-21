# cook your dish here
t=int(input())
if t>=1 and t<=1000:
    for _ in range(t):
        n,x=map(int,input().split())
        if n>=1 and n<=100 and x>=1 and x<=1000:
            cost=x*(n//6)
            if int(n/6)==n/6:
                print(cost)
            else:
                cost+=x
                print(cost)