def knock(func):
    data = [40]
    f = lambda x: print('x is')
    def wrapper():
        print("Knock Knock!")
        func()
        f(2)
        print('data is ',data[0])
        print("Knock Knock!")
        data[0] = data[0] + 1
    return wrapper

knock_penny = knock(lambda: print("Penny"))

print(knock.__closure__) # None because it's not a closure

print("deleting knock") # deleting the outer function

del knock

print("type of knock penny",type(knock_penny)) #type of knock penny <class 'function'>

knock_penny() # knock knock! \n Penny \n data is 40 \n Knock Knock!
knock_penny() # knock knock! \n Penny \n data is 41 \n Knock Knock! # Hence function in Python is also mutable


print("closure of knock_penny", knock_penny.__closure__)  #closure of knock_penny 
                                                          #(<cell at 0x000001998A432CA0: list object at 0x000001998A3E67C0>, 
                                                          # <cell at 0x000001998A432CD0: function object at 0x000001998A7398B0>, 
                                                          #<cell at 0x000001998A432D00: function object at 0x000001998A7394C0>)
                                                          
print("data in closure", knock_penny.__closure__[0].cell_contents) # data in closure [42]
print("f in closure", knock_penny.__closure__[1].cell_contents) # f in closure <function knock.<locals>.<lambda> at 0x000001E81D5498B0>


