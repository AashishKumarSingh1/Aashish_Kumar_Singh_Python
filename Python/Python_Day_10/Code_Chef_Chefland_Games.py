# cook your dish here
t=int(input())
if t in range(1,21):
    for _ in range(t):
        r1,r2,r3,r4=map(int,input().split())
        if (r1 and r2 and r3 and r4) in range(0,2):
            sum=r1+r2+r3+r4
            if sum==0:
                print('IN')
            else:
                print('OUT')
                
