t=int(input())
if t in range(1,50):
    for i in range(t):
        x = int(input())
        if x in range(1,301):
            if x in range (1,100):
                print("Easy")
            elif x in range(100,200):
                print("Medium")
            elif x in range(200,301):
                print("Hard")
            else:
                pass
else:
    pass
    
"""
admin -> x points

easy 
medium 
hard 


"""
