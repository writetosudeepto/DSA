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
            merge.append(right[j])
            j+=1
    if i<len(left):
        merge.extend(left[i:])
    if j<len(right):
        merge.extend(right[j:])
   
    return merge

print(merge_sort([5,4,6,3,2,3,2,1]))


