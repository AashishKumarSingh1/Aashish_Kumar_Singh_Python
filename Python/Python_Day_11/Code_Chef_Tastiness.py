# cook your dish here
t=int(input())
if t>=1 and t<=100:
    for _ in range(t):
        a,b,c,d=map(int,input().split())
        if (a and b and c and d) in range(1,101):
            tastiness=max(a,b)+max(c,d)
            print(tastiness)