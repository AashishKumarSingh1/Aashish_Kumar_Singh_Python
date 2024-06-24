# cook your dish here
t=int(input())
if 1<=t<=1000:
    for _ in range(t):
        n,x,p=map(int,input().split())
        if 1<= n <=100 and 0<=x<=n and 0<=p<=3*n:
            chef_score=x*3+(n-x)*-1
            if chef_score>=p:
                print('Pass')
                pass
            else:
                print('Fail')
                pass