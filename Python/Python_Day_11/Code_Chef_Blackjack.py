# cook your dish here
t=int(input())
if t>=1 and t<=100:
    for _ in range(t):
        a,b=map(int,input().split())
        if (a and b)>=1 and (a and b)<=10:
            third=21-a-b
            if third>=1 and third<=10:
                print(third)
                pass
            else:
                print('-1')
                pass
            