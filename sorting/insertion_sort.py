def insertion_sort(arr):
    for i in range(1, len(arr)):
        index_to_insert = i
        j = i - 1
        while j >= 0:
            if arr[j] < arr[index_to_insert]:
                break
            print("swapping {} and {}".format(arr[j], arr[index_to_insert]))
            arr[j],arr[index_to_insert] = arr[index_to_insert],arr[j]
            print("array is now {}".format(arr))
            index_to_insert = j
            j -= 1
    return arr

print(insertion_sort([5,4,6,3,2,3,2,1]))