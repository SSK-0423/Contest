n = int(input())
ans = 'Yes'
w = []
for i in range(n):
    w.append(input())
for i in range(0,n-1):
    if w.count(w[i]) > 1:
        ans = 'No'
        break
    elif w[i][-1] != w[i+1][0]:
        ans = 'No'
        break
print(ans)