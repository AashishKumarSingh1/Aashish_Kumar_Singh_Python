# cook your dish here
x,y=map(int,input().split())
if (x and y) in range(1,1000) and y%2==0:
    time=(x-y)+y/2 
    print(int(time))