# cook your dish here
t=int(input())
if t in range(1,101):
    for _ in range(t):
        x,y=map(int,input().split())
        if x and y in range(1,1001):
            max_bag=x*y //100
            print(max_bag)
    
