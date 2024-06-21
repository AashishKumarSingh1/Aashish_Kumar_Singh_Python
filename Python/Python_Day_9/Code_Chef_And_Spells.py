t=int(input())
if t in range(1,(pow(10,4))+1):
    for i in range(t):
        a,b,c = map(int,input().split())
        if a in range(1,pow(10,8)+1) and b in range(1,pow(10,8)+1) and c in range(1,pow(10,8)+1):
            #input form => 4,2,8 :: output=> 12
            hit_points=0
            total_points=a+b+c
            max_hit_points=total_points-min(a,b,c)
            print(max_hit_points)
        else:
            pass
else:
    pass
