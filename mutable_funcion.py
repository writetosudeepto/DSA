def outer(data):
    def inner(f):
        nonlocal data
        data=f(data)
        def myfun():
            print(data)
        return myfun
    return inner
wrap1 = outer(1000)
# del outer # deleting the outer function so that the scope of inner function should also be lost
# print('current data: ',wrap.__closure__[0].cell_contents) # 40
# newdata = wrap(lambda x: x+1) # 41
# print('new data: ',newdata) # 42
# newdata = wrap(lambda x: x+2) #43
# print('updated data: ',wrap.__closure__[0].cell_contents) # 41
# wrap.__closure__[0].cell_contents += 1
# print('updated data after mutation: ',wrap.__closure__[0].cell_contents) # 42
# x = wrap1(lambda x: x+1)
# y = wrap1(lambda x: x+2)
# z = wrap1(lambda x: x+3)
# data = [x, y, z]
# print("data: ",data)
# for el in data:
#     el()
wrap1(lambda x: x+1)()
wrap1(lambda x: x+2)()
wrap1(lambda x: x+3)()