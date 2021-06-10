n = int(input())
p = list(map(int,input().split()))
count = 0
a = list(range(1,n+1))
for i in range(n):
    if p[i] != a[i]:
        count += 1
if count <= 2:
    print('YES')
else:
    print('NO')

