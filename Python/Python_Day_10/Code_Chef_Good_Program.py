# cook your dish here
t=int(input())
if t in range(1,1001):
    for _ in range(t):
        n=int(input())
        if n in range(1,1001):
            if n//4 == (n/4):
                print("Good")
            else:
                print("Not Good")