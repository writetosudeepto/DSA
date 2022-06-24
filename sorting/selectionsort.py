def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:        # saves a swap if i and min_index are the same
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([5,4,6,3,2,3,2,1]))