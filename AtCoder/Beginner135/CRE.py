n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
count = 0
for i in range(n-1,-1,-1):
    # i+1の討伐
    if a[i+1] < b[i]:
        count += a[i+1]
        b[i] -= a[i+1]
        a[i+1] = 0
    else:
        count += b[i]
        a[i+1] -= b[i]
        b[i] = 0
    # iの討伐
    if a[i] < b[i]:
        count += a[i]
        b[i] -= a[i]
        a[i] = 0
    else:
        count += b[i]
        a[i] -= b[i]
        b[i] = 0
print(count)
