n,x = map(int,input().split())
l = list(map(int,input().split()))
d = 0 #1回目の座標
#2回目以降
count = 1
for i in range (0,n):
    d = d + l[i]
    if(d > x):
        break
    count += 1

print(count)
