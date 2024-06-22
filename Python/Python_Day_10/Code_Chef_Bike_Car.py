# cook your dish here
t=int(input())
if t in range(1,101):
    for _ in range(t):
        x,y=map(int,input().split())
        if (x and y) in range(1,11):
            if x==y:
                print("SAME")
            elif x>=y:
                print('CAR')
            elif x<=y:
                print('BIKE')
            else:
                pass
            