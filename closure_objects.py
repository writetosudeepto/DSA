def outer(data):
    def inner(f):
        nonlocal data
        def fun():
            nonlocal f
            nonlocal data
            data = f(data)
            print("inside fun: ",data)
            def morefun():
                nonlocal f
                nonlocal data
                class ExtraFun:
                    def play(self,f2):
                        print("displaying data: ",self.data)
                        inp = input("Do you want to apply the second func? (y/n) ")
                        if inp == 'y':
                            self.data = f2(self.data)
                            self.play(f2)
                        else:
                            print("Thanks for using!")
                    def __init__(self):
                        self.data = data
                        self.extrafun = f
                nonlocal data
                nonlocal f
                data = f(data)
                print("inside more fun: ",data)
                return ExtraFun()
            return morefun
        return fun
    return inner
wrap = outer(1000)
wrap(lambda x: x*20)()().play(lambda x: x*10)