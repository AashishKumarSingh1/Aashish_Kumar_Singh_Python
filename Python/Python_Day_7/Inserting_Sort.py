def insertion_sort(arr):
    # Traverse from the second element to the end of the array
    for i in range(1, len(arr)):
        temp = arr[i]
        current_pointer = i - 1
        
        # Move elements of arr[0..i-1], that are greater than temp,to one position ahead of their current position
        while current_pointer >= 0 and arr[current_pointer] > temp:
            arr[current_pointer + 1] = arr[current_pointer]
            current_pointer -= 1
        
        # Place temp in its correct position
        arr[current_pointer + 1] = temp
    
    return arr

arr = [74, 11, 7, 14, 35]
sorted_arr = insertion_sort(arr)

print("After Insertion Sort Array becomes:", sorted_arr)



























# #Insertion Sorting Algorithm 

# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         current_value=arr[i]
#         current_pointer=i
        
#         while current_pointer>0 and arr[current_pointer-1]>current_value:
#             arr[current_pointer]=arr[current_pointer-1]
#             current_pointer=current_pointer-1
#             arr[current_pointer]=current_value
            
#     return arr

# num_arr=[74,11,7]

# print(num_arr)

# insertion_sort(num_arr)

# print(num_arr)