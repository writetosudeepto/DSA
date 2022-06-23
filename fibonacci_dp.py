cal = memos = 0
memo = []
for i in range(20):
    memo.append(-1)
def fib(n):
    global cal, memos
    print("memo:",memo)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if memo[n] == -1:
        cal += 1
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    else:
        memos += 1
        return memo[n]
print(fib(9),"calculations:",cal,"memos:",memos)
    

# memo = []
# for i in range(100000):
#     memo.append(-1)
# count = overlap = 0
# overlaps = []
# def fib(n):
#     global count,overlap
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if memo[n] != -1:
#         overlap += 1
#         overlaps.append(n)
#         return memo[n]
#     count += 1
#     memo[n] = fib(n-1) + fib(n-2)
#     return memo[n]

# print(fib(800),"calculations:",count, "overlap:",overlap,"overlaps:",overlaps)

# output: 8