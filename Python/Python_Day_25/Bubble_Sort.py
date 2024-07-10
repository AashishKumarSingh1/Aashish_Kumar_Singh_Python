def Bubble_Sort(list_1):
    n = len(list_1)
    for i in range(n):

        swapped = False
        for j in range(0, n-i-1):
            if list_1[j] > list_1[j+1]:
                list_1[j], list_1[j+1] = list_1[j+1], list_1[j]
                swapped = True

        if not swapped:
            break
    return list_1

list_1 = [64, 34, 25, 12, 22, 11, 90]
sorted_list = Bubble_Sort(list_1)
print("Sorted list:", sorted_list)
