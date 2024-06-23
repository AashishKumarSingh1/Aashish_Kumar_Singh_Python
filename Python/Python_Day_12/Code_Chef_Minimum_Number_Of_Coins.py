# cook your dish here
t=int(input())
if t>=1 and t<=1000:
    for _ in range(t):
        x=int(input())
        if x%5==0:
            print(x//10+(x%10)//5)
            pass
        else:
            print('-1')