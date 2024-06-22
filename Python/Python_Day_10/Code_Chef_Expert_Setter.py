# cook your dish here
t=int(input())
if t in range(1,1001):
    for _ in range(t):
        x,y=map(int,input().split())
        if y in range(1,x+1) and x in range(y,(10**6)+1):
            problem_percent=(y)*100/x 
            if problem_percent>=50:
                print("YES")
            else:
                print("NO")
