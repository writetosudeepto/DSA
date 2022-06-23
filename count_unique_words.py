def count_unique_words(inp):
    count = 0
    for word in inp.split():
        st = set(word)
        if len(st)==len(word):
            count +=1
    return count

print(count_unique_words('hello hey ther hello hello'))