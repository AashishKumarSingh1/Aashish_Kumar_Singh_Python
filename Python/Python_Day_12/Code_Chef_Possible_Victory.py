# cook your dish here
r,o,c=map(int,input().split())
if 0<=c<=r<=720 and 1<=o<=19 and 0<=c<=36*o:
    # (r-c)run in 20-o over
    if ((20-o)*6)*6 + (c) >r:
        print("Yes")
        pass
    else:
        print("no")
