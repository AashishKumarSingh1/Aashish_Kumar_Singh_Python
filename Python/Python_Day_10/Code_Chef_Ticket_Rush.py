# cook your dish here
t=int(input())
if t>=1 and t<=1001:
    for _ in range(t):
        n,m=map(int,input().split())
        if n>=1 and m>=1 and m<=10**5 and n<=10**5:
            if n<m:
                print('0')
                pass
            else:
                print(n-m)