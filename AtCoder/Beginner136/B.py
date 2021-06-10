n = int(input())
num = list(range(1,n+1))
count = 0
for i in num:
    if i < 10 or (i >= 100 and i < 1000) or (i >= 10000 and i < 100000):
        count += 1
print(count)