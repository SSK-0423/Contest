a,b,k = map(int,input().split())
num = []
if k >= b:
    for i in range(a,b+1):
        print(i)
else:
    for i in range(k):
        num.append(a+i)
    for i in range(k-1,-1,-1):
        if (b - i) in num:
            pass
        else:
            num.append(b - i)
    for i in num:
        print(i)