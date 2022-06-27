def insertion_sort(arr):
    iter_count = 0
    for i in range(1, len(arr)):
        index_to_insert = i
        j = i - 1
        while j >= 0:
            iter_count += 1
            if arr[j] < arr[index_to_insert]:
                break
            print("swapping {} and {}".format(arr[j], arr[index_to_insert]))
            arr[j],arr[index_to_insert] = arr[index_to_insert],arr[j]
            print("array is now {}".format(arr))
            index_to_insert = j
            j -= 1
    return arr,iter_count

print(insertion_sort([1,2,3,4,5,6,7,8,9]))