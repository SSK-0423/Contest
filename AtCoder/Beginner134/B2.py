n,d = map(int,input().split())
a = n // (2*d+1)
b = n % (2*d+1)
if b:
    print(a+1)
else:
    print(a)