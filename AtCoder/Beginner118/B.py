n,m = map(int,input().split())
data = []
count = 0
a = 0
for i in range(n):
    data.append(list(map(int,input().split())))
for i in range(m):
    for j in range(n):
        a += data[j][1:].count(i+1)
    if a == n:
        count += 1
    a = 0
print(count)