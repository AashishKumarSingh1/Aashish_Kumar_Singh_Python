# cook your dish here
t=int(input())
if 1<=t<=1000:
    for _ in range(t):
        n=int(input())
        if 1<=n<=1000:
            group=n//7 
            if (n%7)%7>=2:
                group+=1 
            print(group)