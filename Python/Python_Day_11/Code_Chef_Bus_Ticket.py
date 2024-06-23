# cook your dish here
t=int(input())
if t>=1 and t<=300:
    for _ in range(t):
        n=int(input())
        if n>=1 and n<=30:
            if n in range(1,16):
                if n in range(1,11):
                    print("Lower Double")
                else:
                    print("Lower Single")
            elif n in range(16,31):
                if n in range(16,26):
                    print("Upper Double")
                    pass
                else:
                    print("Upper Single")
                    pass
            else:
                pass
            