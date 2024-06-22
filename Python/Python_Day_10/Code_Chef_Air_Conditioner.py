# cook your dish here
t=int(input())
if t in range(1,101):
    for _ in range(t):
        a,b,c=map(int,input().split())
        if (a and b and c ) in range(1,101):
            agree=0 
            a=max(a,c)
            list=[i for i in range(a,b+1)]
            if (len(list)>0):
                print('Yes')
            else:
                print('No')
            