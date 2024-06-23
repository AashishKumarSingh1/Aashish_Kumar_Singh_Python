# cook your dish here
t = int(input())
if 1 <= t <= 10**4:
    for _ in range(t):
        w, x, y, z = map(int, input().split())
        if all(1 <= val <= 10**5 for val in (w, x, y, z)):
            weights = [x, y, z]
            found = False
            for i in range(1 << 3):  # 1 << 3 is 2^3 which is 8 (all subsets)
                sum_weights = 0
                for j in range(3):
                    if i & (1 << j):
                        sum_weights += weights[j]
                if sum_weights == w:
                    found = True
                    break
            
            if found:
                print("Yes")
            else:
                print("No")
