# cook your dish here
t=int(input())
if t in range(1,1001):
    for _ in range(t):
        # a,b,c,d=map(int,integer.split())
        a,b=map(int,input().split())
        c,d=map(int,input().split())
        
        if (a and b and c and d) in range(0,11):
            if (a<=c) and (b<=d):
                print("POSSIBLE")
            else:
                print('IMPOSSIBLE')