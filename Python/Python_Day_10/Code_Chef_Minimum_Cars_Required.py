# cook your dish here
t=int(input())
if t in range(1,1001):
    for _ in range(t):
        n=int(input())
        no_car=n//4 
        if n%4==0:
            print(no_car)
        else:
            print(no_car+1)