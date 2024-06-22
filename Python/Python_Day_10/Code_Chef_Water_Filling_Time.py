# cook your dish here
t=int(input())
if t in range(1,1001):
    for _ in range(t):
        b1,b2,b3=map(int,input().split())
        if (b1 and b2 and b3) in range(0,2):
            sum=b1+b2+b3
            #fill :: <=1 
            if sum<=1:
                print("Water filling time")
            else:
                print("Not now")