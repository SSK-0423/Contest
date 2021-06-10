
n = int(input())
s = []
for i in range(n):
    s.append(input())
count = 0
for i in range(n):
    s[i] = ''.join(sorted(s[i]))
for i in s:
    count += s.count(i)
print(count)