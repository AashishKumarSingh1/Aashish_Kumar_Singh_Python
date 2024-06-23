# cook your dish here
t=int(input())
if t>=1 and t<=1000:
    for _ in range(t):
        s,x,y,z=map(int,input().split())
        #9 4 5 1 
        if s>=1 and s<=500 and z<=s and (x+y)<= s and x>=1 and x<=y and y<=s:
            max_space=max(x,y)
            left_space=s-x-y
            if left_space>=z:
                print('0')
                pass
            elif (left_space+max_space)>=z:
                print('1')
                pass
            else:
                print('2')
            