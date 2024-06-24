#cook your dish here
import math
t = int(input())
if 1 <= t <= 1000:
    for _ in range(t):
        x, y = map(int, input().split())
        if 1 <= x <= 100 and 1 <= y <= 100 and x != y:
            # Calculate the floor number for room x and room y
            floor_x = (x - 1) // 10 + 1
            floor_y = (y - 1) // 10 + 1
            floors_to_travel = abs(floor_x - floor_y)
            # Print the result
            print(floors_to_travel)
