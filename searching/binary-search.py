def binary_search(lst,el) -> int:
    start = lst[0]
    end = lst[-1]
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == el:
            return mid
        elif lst[mid] > el:
            end = mid - 1
        else:
            start = mid + 1
    return -1