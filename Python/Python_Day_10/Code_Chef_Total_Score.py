# cook your dish here
t=int(input())
if t in range(1,101):
    for _ in range(t):
        n,x,y= map(int,input().split())
        if (n and x ) in range(1,11) and y in range(0,(n*x)+1):
            total_marks=0
            for i in range(n+1):
                if y==0:
                    print("YES")
                    break
                total_marks+=x 
                if(total_marks==y):
                    print("YES")
                    break
                else:
                    pass
                
                
            
                
            if (total_marks!=y):
                 print("NO")
            