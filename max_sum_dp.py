a = [3,2,3,5]
memo = {}
def max_sum(i=len(a)-1):
    if i == 0:
        return a[i]
    elif i == 1:
        return max(a[i-1],a[i])
    else:
        if i in memo:
            return memo[i]
        else:
            memo[i] = max(max_sum(i-1),a[i]+max_sum(i-2))
            return memo[i]
print(max_sum(),"memo: ",memo)
