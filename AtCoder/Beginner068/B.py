n = int(input())
ans = []
for i in range(1,n+1):
    count = 0
    num = i
    while True:
        if num % 2 == 0:
            count += 1
        else:
            break
        num /= 2
    ans.append(count)
print(ans.index(max(ans))+1)