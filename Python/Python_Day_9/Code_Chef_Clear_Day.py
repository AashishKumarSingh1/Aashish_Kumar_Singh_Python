# cook your dish here
x,y=map(int,input().split())
if x in range(0,8) and y in range(0,8) and (x+y) in range (0,8):
    clear=7-x-y
    print(clear)
    