# cook your dish here
import math
for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    even_count = sum(1 for num in a if num % 2 == 0)
    odd_count = n - even_count  # Total elements minus even elements gives odd elements

    if even_count == 0:
        # All elements are already odd
        print(0)
    elif x % 2 == 1:
        # If X is odd, we can make two even numbers odd in one operation
        print((even_count + 1) // 2)
    else:
        if odd_count == 0:
            # If there are no odd numbers and X is even, it's impossible
            print(-1)
        else:
            # Each operation will turn one even number into odd
            print(even_count)