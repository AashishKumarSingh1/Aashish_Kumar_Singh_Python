# Cook your dish here
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if x >= y:
        print(0)
    else:
        month = (y - 1) // x
        print(month)
