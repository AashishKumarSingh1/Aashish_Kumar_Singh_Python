# cook your dish here
for _ in range(int(input())):
    n = int(input())
    goal = list(map(int, input().split()))

    max_diff = 0
    min_goal = goal[0]

    for i in range(1, n):

        diff_n = goal[i] - min_goal
        if diff_n > max_diff:
            max_diff = diff_n

        if goal[i] < min_goal:
            min_goal = goal[i]

    if max_diff > 0:
        print(max_diff)
    else:
        print("UNFIT")
