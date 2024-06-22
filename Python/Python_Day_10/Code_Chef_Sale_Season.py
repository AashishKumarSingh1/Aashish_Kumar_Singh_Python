# cook your dish here
t=int(input())
if t in range(1,101):
    for _ in range(t):
        x = int(input())
        final_amount=x
        if x<=100:
            print(final_amount)
        elif x in range(101,1001):
            final_amount=x-25
            print(final_amount)
        elif x in range(1001,5001):
            final_amount=x-100
            print(final_amount)
        elif x>5000:
            print(x-500)
        else:
            pass
        
            