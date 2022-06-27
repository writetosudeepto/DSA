def merge_sort(ar):
    if len(ar)<=1:  # base case
        return ar
    n = len(ar)
    i,j = 0,0
    left = merge_sort(ar[:n//2])
    right = merge_sort(ar[n//2:])
    merge = []
    while(i<len(left) and j<len(right)):  # while both arrays have elements
        if left[i]<right[j]:
            merge.append(left[i])
            i+=1
        else:
            ar[i+j] = right[j]
            merge.append(right[j])
            j+=1
    while(i<len(left)):   # while left array has elements
        merge.append(left[i])
        i+=1
    while(j<len(right)):  # while right array has elements
        merge.append(right[j])
        j+=1
    return merge


