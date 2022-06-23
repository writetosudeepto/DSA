def find_substr_index(string, substring):
    if substring in string:
        return string.index(substring)
    else:
        return -1