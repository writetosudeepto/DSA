def outer(data, f):
    con = 100
    def inner():
        nonlocal data
        nonlocal f
        nonlocal con
        def increase_and_showcon():
            nonlocal con
            nonlocal data
            con += data
            print("con: ",con)
        def inner_inner(inner_ref):
            nonlocal data
            nonlocal f
            nonlocal con
            nonlocal increase_and_showcon
            data = inner_ref.__closure__[2].cell_contents(data)
            print(data)
        return inner_inner
    return inner
x = outer(10, lambda x: x+1)()
x(x)
x.__closure__[3].cell_contents()
x(x)
x.__closure__[3].cell_contents()