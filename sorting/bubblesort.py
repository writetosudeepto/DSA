def optimized_bubblesort(arr):
    swap_count = 0
    for i in range(len(arr)):
        is_sorted = True
        for j in range(len(arr)-i-1):
            # print("i is",i,"j is",j)
            print("comparing",arr[j],"and",arr[j+1])
            if arr[j] > arr[j+1]:
                print("swapping",arr[j],"and",arr[j+1])
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_sorted = False
                swap_count += 1
            print("current array is",arr)
        if is_sorted:
            break
    return arr,swap_count

print(optimized_bubblesort([9,5,7,1,3,2,4,6,8]))