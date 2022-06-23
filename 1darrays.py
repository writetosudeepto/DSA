t = int(input())
for i in range(t):
    ar = list(map(int,input().split()))
    ans = 0
    element = int(input())
    for j in ar:
        if j == element:
            ans = 1
            break
    print(ans)