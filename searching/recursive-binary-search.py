def binary_search(arr,item):
    def binary_search_recursive(arr,item,start,end,):
        if start > end:
            return -1
        else:
            mid = (start+end) // 2
            if arr[mid] == item:
                return mid
            elif item < arr[mid]:
                return binary_search_recursive(arr,item,start,mid-1)
            else:
                return binary_search_recursive(arr,item,mid+1,end)
    return binary_search_recursive(arr,item,0,len(arr)-1)