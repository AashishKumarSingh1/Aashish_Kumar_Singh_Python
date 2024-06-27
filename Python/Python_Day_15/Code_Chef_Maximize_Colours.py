for _ in range(int(input())):
    x,y,z=map(int,input().split())
    primary_color=0 
    if x>=1:
        primary_color+=1 
        x-=1 
    if y>=1:
        primary_color+=1 
        y-=1 
    if z>=1:
        primary_color+=1 
        z-=1 
    secondary_color=0 
    color=[x,y,z]
    color.sort()
    x=color[-1]
    y=color[-2]
    z=color[-3]
    if x>0 and y>0:
        pair=min(x,y)
        secondary_color+=1
        x-=1
        y-=1
    if z>0 and y>0:
        pair=min(y,z)
        secondary_color+=1
        z-=1
        y-=1
    if x>0 and z>0:
        pair=min(x,z)
        secondary_color+=1
        z-=1
        y-=1
    print(primary_color+secondary_color)