n,m = map(int,input().split())

l = [0]*100000
r = [0]*100000
b = [0]*(n + 2)

count = 0

for i in range(0,m):
    l[i],r[i] = map(int,input().split())

for i in range(0,m):
    b[l[i]] = 1
    b[r[i] + 1] = -1
    
print(b)

#最小値を調べる
for i in range(0,n+2):
    if(b[i] == 1 or b[i] == -1):
        min_n = i
        break
#最大値を調べる
for i in range(n+1,0,-1):
    if(b[i] == 1 or b[i] == -1):
        max_n = i
        break
print(min_n)
print(max_n)
for i in range(min_n,max_n):
    if(b[i] == 0):
        count += 1

print(count)
