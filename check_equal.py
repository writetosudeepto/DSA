def left_shift(st):
    st = st[1:] + st[0]
    return st



print(left_shift('abcde'))