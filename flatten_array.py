def flatten(arr):
    flat_list = []
    for i in arr:
        if isinstance(i, list):
            flat_list.extend(flatten(i))
        else:
            flat_list.append(i)
    flat_list.sort()
    return flat_list

print(flatten([10,[20,40],30,50]))