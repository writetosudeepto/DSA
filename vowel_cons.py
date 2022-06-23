n = int(input())
vowels = ('a','e','i','o','u')
for i in range(n):
    word = input()
    vows= 0
    cons = 0
    for l in word:
        l = l.lower()
        print(l,type(l))
        if l in vowels:
            vows += 1
        else:
            cons += 1
    print(vows,cons)
