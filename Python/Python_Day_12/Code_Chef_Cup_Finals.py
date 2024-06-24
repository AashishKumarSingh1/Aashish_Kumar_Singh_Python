# cook your dish here
t=int(input())
if 1<=t<=2000:
    for _ in range(t):
        x,y,d=map(int,input().split())
        if 1<= (x and y) <=100 and 0<=d<=100:
            if ( abs (x-y)<= d):
                print('Yes')
                pass
            else:
                print('no')
                pass
            
            