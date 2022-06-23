def array_right_shift(arr):
    arr.insert(0,arr.pop())
    return arr

print(array_right_shift([1,2,3,4,5]))
                    