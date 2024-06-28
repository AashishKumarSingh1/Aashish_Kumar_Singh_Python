#Approach 1 
for _ in range(int(input())):
    n, h, y1, y2, l = map(int, input().split())
    barrier_pass = 0 
    for i in range(n):
        ti, x = map(int, input().split())
        
        if (ti == 1 and (h <= x or x >= y1) and l > 0):
            barrier_pass += 1 
        elif (ti == 2 and y2 >= x and l > 0):
            barrier_pass += 1 
        elif (ti == 1 and y1 < x and l > 0):
            barrier_pass += 1 
            l -= 1
        elif (ti == 2 and x > y2 and l > 0):
            barrier_pass += 1 
            l -= 1 

    print(barrier_pass)

#Approach 2 
for _ in range(int(input())):
    n,height,y1,y2,l=map(int,input().split())
    counter=0
    for i in range(n):
        t,x=map(int,input().split())
        if t==1:
            if (height-y1)>x:
                l-=1
        else:
            if y2<x:
                l-=1
        if l>=1:
            counter+=1
    print(counter)