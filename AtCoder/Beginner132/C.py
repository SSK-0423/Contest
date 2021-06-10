N = int(input())
d = list(map(int,input().split()))

max_k = max(d)
min_k = min(d)

d.sort()

abc = []
arc = []
count = 0

for k in range(min_k,max_k + 1):
    abc = [num for num in range(0,N) if d[num] < k]
    arc = [num for num in range(0,N) if d[num] >= k]
    if(len(abc) == len(arc)):
        count += 1
print(count)

