# cook your dish here
t=int(input())
if 1<=t<=2500:
    for _ in range(t):
        a,b,x,y=map(int,input().split())
        if 1<=( a and b )<=100 and 1<=(x and y)<=10:
            chef_time=a/x 
            chefina_time=b/y 
            if chefina_time>chef_time:
                print("Chef")
                pass
            elif chef_time>chefina_time:
                print("Chefina")
                pass
            else:
                print("Both")