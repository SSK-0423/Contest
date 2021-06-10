import copy
n,l = map(int,input().split())
taste = []
for i in range(0,n):
    taste.append(l + i + 1 -1)

all_t = sum(taste)

save = copy.copy(taste)
azi = []

for i in range(0,n):
    del taste[i]
    azi.append(abs(all_t - sum(taste)))
    taste  = copy.copy(save)

a = azi.index(min(azi))
del taste[a]
print(sum(taste))


