n = int(input())
h = list(map(int,input().split()))
now = h[0] - 1
can = True
for i in range(1,n):
    if now == h[0]:
        pass
    elif now < h[i]:
        now = h[i] - 1
    else:
        can = False
        break
if can:
    print('Yes')
else:
    print('No')