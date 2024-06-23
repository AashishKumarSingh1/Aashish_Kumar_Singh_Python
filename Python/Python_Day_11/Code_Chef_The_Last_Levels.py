# cook your dish here
t=int(input())
if t>=1 and t<=100:
    for _ in range(t):
        x,y,z=map(int,input().split())
        if x>=1 and x<=100 and y>=5 and y<=100 and z>=5 and z<=15:
            if x%3==0:
                complete_time=x*y + (x-3)//3*z
                print(complete_time)
                pass
            else:
                complete_time=x*y+(x)//3 *z
                print(complete_time)