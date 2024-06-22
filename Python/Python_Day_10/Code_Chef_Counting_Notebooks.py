# cook your dish here
t=int(input())
if t in range(1,101):
    for _ in range(t):
        n=int(input())
        if n in range(1,101):
            notebook=(n*1000)//100
            print(notebook) 