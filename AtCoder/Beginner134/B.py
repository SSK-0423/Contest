n,d = map(int,input().split())
tree = list(range(n))
count = 0
for i in range(2*d+1,n+1,2*d+1):
    count += 1
    if (n - i <= 2*d + 1):
        count += 1
        break
print(count)