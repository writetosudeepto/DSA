memo = {}
def getWays(n, c):
    key = (n, tuple(c))
    if len(c)==0:
        return 0
    if n<0:
        return 0
    if n==0:
        return 1
    else:
        if key in memo:
            return memo[key]
        else:
            memo[key] = getWays(n-c[0],c) + getWays(n,c[1:])
            return memo[key]