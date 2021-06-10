a,b = map(int,input().split())

x = (a + b) / 2 #商
c = (a + b) // 2 #商の整数部

if((x - c) > 0):
    print(c + 1)
else:
    print(c)