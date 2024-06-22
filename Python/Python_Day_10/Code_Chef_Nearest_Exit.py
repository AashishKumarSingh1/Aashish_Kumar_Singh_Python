# cook your dish here
t=int(input())
if t in range(1,101):
    for _ in range(t):
        x=int(input())
        if x in range(1,101):
            left=x-1
            right=100-x
            if left>right:
                print("RIGHT")
            else:
                print('LEFT')