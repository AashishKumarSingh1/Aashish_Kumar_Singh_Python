def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element
        min_idx = i
        # Iterate through the unsorted elements
        for j in range(i + 1, n):
            # Find the smallest element
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [5, 4, 3, 2, 1]
selection_sort(arr)
print("After Selection Sort: ", arr)
