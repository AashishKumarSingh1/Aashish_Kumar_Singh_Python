# cook your dish here
t=int(input())
if t>=1 and t<=1000:
    for _ in range(t):
        n,m=map(int,input().split())
        if (n and m)<=1000 and (n and m)>=1:
            if n<m:
                print('No')
                continue
            if (n%m)==0 and (n//m)%2==0:
                print('yes')
                pass
            else:
                print('No')