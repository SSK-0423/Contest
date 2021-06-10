s = input()
ans = []
for x in s:
    if x == 'B' and len(ans):
        ans.pop()
    elif x == 'B' and len(ans) == 0:
        pass
    else:
        ans.append(x)
ans_s = ''
for x in ans:
    ans_s += x
print(ans_s)

