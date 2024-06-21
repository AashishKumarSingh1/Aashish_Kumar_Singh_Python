# cook your dish here
t=int(input())
if t>=1 and t<=2*10**4:
    for _ in range(t):
        x,y,z=map(int,input().split())
        if x in range(1,6) and y in range(1,51) and z in range(0,(x*y)+1):
            total_students=x*y
            pass_percent=(z)*100/total_students
            
            if pass_percent>50:
                # print(pass_percent)
                print('YES')
            else:
                # print(pass_percent)
                print('NO')
            
            
    