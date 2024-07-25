def Odd(nums: list) -> int:
    c_diff = [nums[i+1] - nums[i] for i in range(len(nums) - 1)]
    count_list = calc_count(c_diff)

    sort_list = sorted(count_list.items(), key=lambda x: x[1], reverse=True)

    index = c_diff.index(sort_list[0][0]) + 1
    return nums[index] if nums[index] in nums else None

def calc_count(lists: list) -> dict:
    # Count the occurrences of each element
    count_list = {}
    for num in lists:
        if num in count_list:
            count_list[num] += 1
        else:
            count_list[num] = 1
    return count_list

print(Odd([1, 2, 3, 4, 6])) 
