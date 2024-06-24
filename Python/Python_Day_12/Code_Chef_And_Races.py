# cook your dish here
t=int(input())
if 1<=t<=144:
    for _ in range(t):
        x,y,a,b=map(int,input().split())
        if 1<=(x and y and a and b)<=4 and x!=y and a!=b:
            max_gold_medal=2 
            if x==a or x==b :
                max_gold_medal-=1 
                pass
            else:
                pass
            
            if y==b or y==a:
                max_gold_medal-=1 
                pass 
            else:
                pass
            print(max_gold_medal)
            