n = int(input())
a = list(map(int,input().split()))
min_a = 10**9
max_a = 1
for i in a:
    if i < min_a:
        min_a = i
    if i > max_a:
        max_a = i
print(max_a - min_a)
