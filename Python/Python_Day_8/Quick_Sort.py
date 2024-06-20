def quick_sort(arr):
    # Base case: an array with 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
        left = [x for x in arr if x < pivot]  # Elements less than the pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
        right = [x for x in arr if x > pivot]  # Elements greater than the pivot
        return quick_sort(left) + middle + quick_sort(right)

arr = [5, 4, 3, 2, 1]
sorted_arr = quick_sort(arr)
print("Sorted Array:", sorted_arr)
