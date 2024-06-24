# Cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    coefficients = list(map(int, input().split()))

    degree = len(coefficients) - 1
    for i in range(len(coefficients)-1, -1, -1):
        if coefficients[i] != 0:
            degree = i
            break

    print(degree)
