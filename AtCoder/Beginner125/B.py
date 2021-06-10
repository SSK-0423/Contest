n = int(input())
v = list(map(int,input().split()))
c = list(map(int,input().split()))
max_num = 0
x = 0
y = 0
for i in range(n):
    if v[i] > c[i]:
        x += v[i]
        y += c[i]
print(x - y)