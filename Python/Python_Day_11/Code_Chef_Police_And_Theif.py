# cook your dish here
t=int(input())
if t in range(1,1001):
    for _ in range(t):
        x,y=map(int,input().split())
        if x>=(-10**5) and x<=10**5 and y<=10**5 and y>=(-10**5):
            
            # police_location=x+2t#t->time
            # theif_location=y+t
            
            t=y-x
            print(abs(t))