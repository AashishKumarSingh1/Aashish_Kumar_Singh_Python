# cook your dish here
t=int(input())
if t in range(1,101):
    for _ in range(t):
        x=int(input())
        if x<=10:
            print("yes")
        else:
            print("no")