# cook your dish here
t=int(input())
if 1<=t<=1000:
    for _ in range(t):
        n=int(input())
        if 0<=n<=20:
            factorial=1 
            for i in range(n,1,-1):
                factorial*=i 
            print(factorial)
        