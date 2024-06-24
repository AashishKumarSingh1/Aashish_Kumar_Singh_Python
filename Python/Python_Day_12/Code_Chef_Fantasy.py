# cook your dish here
t=int(input())
if 1<=t<=10:
    for _ in range(t):
        n=int(input())
        if 2<=n<=11:
            choice=n 
            # for i in range(1,n+1):
            #     choice*=i 
            print(choice*(choice-1))