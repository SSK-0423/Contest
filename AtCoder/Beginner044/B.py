w = input()
only = list(set(w))
count = 0
can = True
for i in only:
    if w.count(i) % 2 != 0:
        can = False
        break
if can:
    print('Yes')
else:
    print('No')