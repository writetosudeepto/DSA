def replace_cube(arr, N):
    for i in range(1,len(arr)+1):
        if i%N==0:
            arr[i-1] = arr[i-1]**3
    return arr

print(replace_cube([1,2,3,4,5],2))