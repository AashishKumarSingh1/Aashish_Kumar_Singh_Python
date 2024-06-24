# cook your dish here
t=int(input())
if 1<=t<=1000:
    for _ in range(t):
        x,y=map(int,input().split())
        total_point_a_to_b=1500-2*x -(x+y)*4
        total_point_b_to_a=1500-2*(x+y)-y*4
        total_point=max(total_point_b_to_a,total_point_a_to_b)
        print(total_point)