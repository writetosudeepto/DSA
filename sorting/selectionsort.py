def selection_sort(arr):
    for i in range(1,len(arr)):
        min_index = i
        j = i-1
        while j>=0:
            if arr[min_index] < arr[j]:
                arr[min_index], arr[j] = arr[j], arr[min_index]
                min_index = j
            j -= 1
    return arr

print(selection_sort([9,5,7,1,3,2,4,6,8]))