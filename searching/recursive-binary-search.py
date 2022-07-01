def binary_search(arr,item):
    def binary_search_recursive(arr,item,low,high,):
        if low > high:
            return -1
        else:
            mid = (low + high) // 2
            if arr[mid] == item:
                return mid
            elif item < arr[mid]:
                return binary_search_recursive(arr,item,low,mid-1)
            else:
                return binary_search_recursive(arr,item,mid+1,high)
    return binary_search_recursive(arr,item,0,len(arr)-1)

print(binary_search([1,2,3,4,5,6,7,8,9,10],1))
