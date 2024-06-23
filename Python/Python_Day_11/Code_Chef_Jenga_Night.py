# cook your dish here
t=int(input())
if t in range(1,10**4 + 1):
    for _ in range(t):
        n,x=map(int,input().split())
        if (n and x) in range(1,1001):
            if x%n==0:
                print('yes')
                pass
            else:
                print('no')
            