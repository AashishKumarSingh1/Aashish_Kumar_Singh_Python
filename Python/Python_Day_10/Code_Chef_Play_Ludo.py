# cook your dish here
t=int(input())
if t in range(1,7):
    for _ in range(t):
        x=int(input())
        if x==6:
            print("Yes")
        else:
            print("No")