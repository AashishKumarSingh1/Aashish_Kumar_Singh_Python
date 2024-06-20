def insertion_sort(arr):

    for i in range(1,len(arr)):
        j=i
        temp=i

        while j>0 and arr[j-1]>arr[temp]:
            arr[temp],arr[j-1]=arr[j-1],arr[temp]
            temp=j-1
            j-=1
    return arr


# arr=[11,7,15,9,12]
arr=[5,4,3,2,1,6,7,8,9,10]
insertion_sort(arr)
print(arr)