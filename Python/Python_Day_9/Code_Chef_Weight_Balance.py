t=int(input())
if t in range(1,pow(10,5)+1):
    for i in range(t):
        w1,w2,x1,x2,m=map(int,input().split())
        # 1 2 1 2 2 :: 0
        if w1 in range(1,w2) and w2 in range(w1+1,101) and x1 in range(0,x2+1) and x2 in range(x1,11) and m in range(1,11):
            increase_weight=w2-w1
            min_inc_wei=x1*m
            max_inc_wei=x2*m
            
            if increase_weight in range(min_inc_wei,max_inc_wei+1):
                print("1")
            else:
                print("0")