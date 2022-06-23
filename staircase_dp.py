def staircase_steps(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return staircase_steps(n-1) + staircase_steps(n-2)

print(staircase_steps(5))