t = int(input())
if 1 <= t <= 1000:
    for i in range(t):
        s, a, b, c = map(int, input().split())
        if 0 <= s <= 10**6 and 0 <= a <= b <= 10**6 and -100 <= c <= 100:
            new_s = s + (c * s) / 100
            if a <= new_s <= b:
                print("Yes")
            else:
                print("No")
