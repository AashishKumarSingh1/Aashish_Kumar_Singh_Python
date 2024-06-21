# cook your dish here
t=int(input())
if t>=1 and t<=10 :
    for _ in range(t):
        x=int(input())
        if x>=1 and x<=9:
            time_left=10-x
            time_required=3
            if time_required>time_left:
                print("No")
            else:
                print('Yes')