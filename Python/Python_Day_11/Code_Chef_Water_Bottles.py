# cook your dish here
t=int(input())
if t>=1 and t<=100:
    for _ in range(t):
        n,x,k=map(int,input().split())
        
        if (n and x ) >= 1 and (n and x )<=10**5 and k>=0 and k<=10**5:
            if n<k//x:
                print(n)
                pass
            else:
                print(k//x)