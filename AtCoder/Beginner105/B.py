n = int(input())
can = False
c = 4
d = 7
for i in range(100//4):
    for j in range(100//7):
        if i * 4 + j * 7 == n:
            can = True
            break
    if can:
        break
if can:
    print('Yes')
else:
    print('No')
    