def merge_sort_with_key(ar, key):
    if len(ar)<=1:  # base case
        return ar
    n = len(ar)
    i,j = 0,0
    left = merge_sort_with_key(ar[:n//2], key=key)
    right = merge_sort_with_key(ar[n//2:], key=key)
    merge = []
    while(i<len(left) and j<len(right)):  # while both arrays have elements
        if key(left[i])<key(right[j]):
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

print(merge_sort_with_key([(7,"Mango"),(1,"Apple"),(3,"Banana"),(4,"Cherry"),(2,"Guava")], key=lambda x: x[0]))