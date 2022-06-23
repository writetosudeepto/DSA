def trim_all_right_left(s,ch):
    while s[0] == ch:
        s = s[1:]
        if s=="":
            return ""
    while s[-1] == ch:
        s = s[:-1]
    return s
print(trim_all_right_left('*****','*'))