t=int(input())
for r in range(t):
    # input format : n,a,b,c
    #a-fruits, b-vegetables, c-fishes
    #d1-> f,v :: d2-> v,f
    n,a,b,c = map(int,input().split())
    if n in range(1, 101) and a in range(1, 101) and b in range(1, 101) and c in range(1, 101):
        d1,d2=0,0
        while (a>0 and b>0) or (b>0 and c>0):
            if a>0 and b>0 :
                d1+=1
                a-=1
                b-=1
            if b>0 and c>0 :
                d2+=1
                b-=1
                c-=1                
              
        if (d1+d2)>=n:
            print("YES")
        else:
            print("NO")
    
    else:
        pass

"""
N guests 
at least one dish serve to each of the n guests

a:1f, 1v

b:1v,1f

chef has : a*f , b*v, c*f

n dishes
"""
