t = int(input())
if t in range(1, pow(10, 5) + 1):
    for i in range(t):
        n, s = map(int, input().split())
        if n in range(1, pow(10, 5) + 1) and s in range(1, (2 * pow(10, 5)) + 1):
            for num in range(n, 0, -1):
                t1 = num
                t2 = s - num
                if t2 in range(n + 1):
                    if t1 - t2 > 0:
                        print(t1 - t2)
                    else:
                        print(-1 * (t1 - t2))
                    break
        else:
            pass
else:
    pass
