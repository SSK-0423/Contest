a,b = map(int,input().split())
num = list(map(str,range(a,b+1)))
count = 0
for i in num:
    if i[::-1] == i:
        count += 1
print(count)