n = int(input("Enter up to how many numbers you want your sum: "))

def recursive_sum(n):
    # base condition
    if n == 1:
        return 1
    
    else:
        return n + recursive_sum(n - 1)

sum_result = recursive_sum(n)
print(sum_result)
