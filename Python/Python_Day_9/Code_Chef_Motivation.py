t=int(input())
if t in range(1,11):
    for i in range(t):
        h_r=0
        n,x=map(int,input().split())
        if n in range(1,(5*pow(10,4))+1) and x in range(1,pow(10,9)+1):
        # print("x is : ",x)
        
            for j in range(n):
           
            
                s_j,r_j=map(int,input().split())
                
                if s_j in range(1,pow(10,9)+1) and r_j in range(1,pow(10,9)+1):
            
                    if s_j<=x:
                        if h_r<r_j:
                            h_r=r_j
                    
                    else:
                        pass
            
        print(h_r)
        
else:
    pass