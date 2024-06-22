
t = int(input())


for _ in range(t):
    n = int(input())
    rev_n = 0
    while n > 0:
        rev_n = rev_n * 10 + n % 10
        n = n // 10
    print(rev_n)
