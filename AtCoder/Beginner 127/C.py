n,m = map(int,input().split())

l = [0]*100000
r = [0]*100000

for i in range(0,m):
    l[i],r[i] = map(int,input().split())

count = 0
num = 0

for key in range(1,n + 1):#鍵の番号
    for i in range(0,m):#
        if(key < l[i]):
            break
        if(key >= l[i] and key <= r[i]):
            count += 1
    if(count == m):
        num += 1
    count = 0
        
print(num)
        
    
