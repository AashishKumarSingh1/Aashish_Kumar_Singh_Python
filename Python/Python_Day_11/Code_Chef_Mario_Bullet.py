# cook your dish here
t=int(input())
if t>=1 and t<=100:
    for _ in range(t):
        x,y,z=map(int,input().split())
        if(x and y and z) in range(1,101) and y%x==0 :
            time_taken=y/x 
            if max(z,time_taken)==z:
                min_time=z-time_taken
                print(int(min_time))
                pass
            else:
                print("0")