n,y = map(int,input().split())

baisu = y // 1000

a = 10
b = 5
flag = 0

for i in range(0,n + 1):
    for j in range(0,n - i + 1):
        num = n - (i + j) #残りの枚数
        total = 10000 * i + 5000 * j + 1000 * num
        if(total == y):
            print(i,j,num)
            flag = 1
            break
    if(flag == 1):
        break
    
if(flag == 0):
    i = -1
    j = -1
    num = -1
    print(i,j,num)
    