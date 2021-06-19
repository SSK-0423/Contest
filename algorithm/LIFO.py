def stack():
    stack = []
    for i in range(0,10):
        stack.append(i)
    print(stack)
    
    b = []
    for i in range(0,10):
        b.append(stack.pop(-1))
    print(b)

stack()