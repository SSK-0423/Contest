n = int(input())
h = list(map(int,input().split()))
can = True
max_n = h[len(h) - 1]
if len(h) > 1:
    for i in range(n-1):
        if not h[i] - 1 <= h[i + 1] or h[i] - 1 > max_n:
                can = False
                break
if can:
    print('Yes')
else:
    print('No')