#Approach 1
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    dir=[]
    for i in range(n):
        dir.append(input())
    dir_rev=list(reversed(dir))
    for i in range(n):
        if i==0:
            dir_rev[i] = dir_rev[i].replace('Right', 'Begin').replace('Left', 'Begin')
        else:
            if i==n-1:
                if dir_rev[i-1].startswith('Left'):
                    dir_rev[i].replace('Begin','Right')
                else:
                    dir_rev[i].replace('Begin','Left')
            elif dir[n-i].startswith('Left'):
                dir_rev[i].replace('Left','Right').replace('Right','Right')
            elif dir[n-i].startswith('Right'):
                dir_rev[i].replace('Right','Left').replace('Left','Left')
        print(dir_rev[i])

#Approach 2
#Cook your dish here
for _ in range(int(input())):
    n = int(input())
    directions = []
    for i in range(n):
        directions.append(input())
    
    dir_rev = list(reversed(directions))
    
    for i in range(n):
        if i == 0:
            dir_rev[i] = dir_rev[i].replace('Right', 'Begin').replace('Left', 'Begin')
        else:
            if directions[n-i].startswith('Left'):
                dir_rev[i] = dir_rev[i].replace('Left', 'Right').replace('Right', 'Right').replace('Begin','Right')
            elif directions[n-i].startswith('Right'):
                dir_rev[i] = dir_rev[i].replace('Right', 'Left').replace('Left', 'Left').replace('Begin','Left')
        
        print(dir_rev[i])
    print()

    
            