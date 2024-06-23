# cook your dish here
t=int(input())
if t>=1 and t<=100 :
    for _ in range(t):
        x=int(input())
        if x>=1 and x<=100:
            transform=['normal','huge','small']
            print(transform[x%3])