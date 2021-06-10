n,m = map(int,input().split())

l = [0]*m
r = [0]*m
b = [0]*(n + 2)

count = 0

for i in range(0,m):
    l[i],r[i] = map(int,input().split())

l_max = max(l)
r_min = min(r)

for i in range(1,n+1):
    if(i >= l_max and i <= r_min ):
        count += 1
        
print(count)
