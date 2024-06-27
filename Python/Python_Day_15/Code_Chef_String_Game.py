# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    
    zeros = s.count('0')
    ones = s.count('1')
    
    if min(zeros, ones) % 2 == 1:
        print("ZLATAN")
    else:
        print("RAMOS")
