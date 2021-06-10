s = input()
ans = ''
for i in range(1,len(s)+1):
    if i % 2 != 0:
        ans += s[i-1]
print(ans)