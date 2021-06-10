n,m,c = map(int,input().split())
b = list(map(int,input().split()))
a = [list(map(int,input().split())) for i in range(n)]
count = 0
ans = 0
for i in range(n):
    for j in range(m):
        ans += a[i][j]*b[j]
    if ans + c > 0:
        count += 1
    ans = 0
print(count)