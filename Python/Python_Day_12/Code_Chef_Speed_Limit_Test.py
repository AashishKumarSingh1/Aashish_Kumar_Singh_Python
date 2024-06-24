# cook your dish here
t=int(input())
if 1<=t<=1000:
    for _ in range(t):
        a,x,b,y=map(int,input().split())
        if 1<=( a and x and b and y)<=1000:
            alice_time=a/x 
            bob_time=b/y  
            if alice_time==bob_time:
                print("EQUAL")
                pass
            elif alice_time>bob_time:
                print('Alice')
                pass
            else:
                print("Bob")