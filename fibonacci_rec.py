count = 0
def fibonacci_rec(n):
    global count
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        count += 1
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)

print(fibonacci_rec(9),"calculations:",count)