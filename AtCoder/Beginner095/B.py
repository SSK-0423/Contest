n,x = map(int,input().split())
m = []
for i in range(n):
    m.append(int(input()))
x -= sum(m)
print(len(m) + x // min(m))