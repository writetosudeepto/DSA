def most_frequent(arr):
    dic = {}
    max_count = 0
    for item in arr:
        count = dic.get(item,0)
        print('item is',item,'count is',count,'max_count is',max_count)
        if count==0:
            dic[item]=1
        else:
            dic[item] +=1
            if dic[item] > max_count:
                max_count = dic[item]
    ans = None
    for key in dic.keys():
        val = dic.get(key)
        print('key is',key,'val is',val)
        if val == max_count:
            ans = key
    return ans

print(most_frequent([1, 3, 2, 1, 4, 1, 3]))