def binary_search(lst,el) -> int:
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == el:
            return mid
        elif lst[mid] > el:
            end = mid - 1
        else:
            start = mid + 1
    return -1