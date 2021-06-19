n = int(input())
a = list(map(int,input().split()))
b = [0]
ans = 0
for i in range(0,n):
    b.append(b[i] + a[i])

b = sorted(b)
print(b)
for i in range(0,n):
    if(i >= 1 and b[i] == b[i-1]):
        ans += 1

print(ans)