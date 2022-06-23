def f(a,b):
    print(a,b)

f(3,5)
from byteplay3 import *
c = Code.from_code(f.__code__)
print(c)