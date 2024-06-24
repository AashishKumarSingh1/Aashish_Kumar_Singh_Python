# cook your dish here
t=int(input())
if 1<=t<=1000:
    for _ in range(t):
        n=int(input())
        if 1<=n<=10**9:
            print(n-n//5)
            
            