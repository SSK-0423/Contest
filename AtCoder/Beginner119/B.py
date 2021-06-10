n = int(input())
m = []
ans = 0
for i in range(n):
    x,u = input().split()
    m.append([float(x),u])
for i in range(n):
    if m[i][1] == 'BTC':
        ans += m[i][0] * 380000.0
    else:
        ans += m[i][0]
print(ans)
