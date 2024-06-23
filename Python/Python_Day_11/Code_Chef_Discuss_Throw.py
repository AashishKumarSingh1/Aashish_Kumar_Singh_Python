# cook your dish here
t=int(input())
if t>=1 and t<=100:
    for _ in range(t):
        a,b,c=map(int,input().split())
        if (a and b and c ) in range(1,101):
            print(max(a,b,c))