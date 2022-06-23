def party(n):
    if n == 1:
        return 1
    elif n==2:
        return 2
    return (n-1) + (n-1)* party(n-2)

print(party(4))