# cook your dish here
for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    array = list(map(abs, array))
    odd_array = [array[i] for i in range(len(array)) if i % 2 == 0]
    even_array = [array[i] for i in range(len(array)) if i % 2 != 0]

    if odd_array and even_array:
        if len(odd_array)>1 and len(even_array)>1:
            min_odd_array = min(odd_array)
            max_even_array = max(even_array)
            odd_array.remove(min_odd_array)
            odd_array.append(max_even_array)
            even_array.remove(max_even_array)
            even_array.append(min_odd_array)
            
        else:
            if even_array[0]>odd_array[0]:
                odd_array[0],even_array[0]=even_array[0],odd_array[0]
                
        
    # print(odd_array,even_array)
    print(sum(odd_array) - sum(even_array))
