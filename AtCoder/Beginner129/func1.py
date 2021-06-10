def f(x):
    return x + 1

def g(x):
    return x ** 2

def add(x,y):
    return x + y

def div35(x):
    return x % 3 == 0 or x % 5 == 0
    
def func(x):
    if x > 100:
        print('BIG')
    else:
        print('SMALL')      

for i in range(1,101):
    print(i,div35(i))
    

    
