# cook your dish here
t=int(input())
if t>=1 and t<=100:
    for _ in range(t):
        n,a,b=map(int,input().split())
        if n>=1 and n<=60 and ( a and b)>=1 and (a and b)<=60:
            total_duration=(n//2)* a + (n-n//2)*b 
            print(total_duration)