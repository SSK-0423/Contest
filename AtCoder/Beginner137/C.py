from math import factorial
n = int(input())
s = []
for i in range(n):
    s.append(input())
count = 0
#---ここまでok
for i in range(n):
    s[i] = ''.join(sorted(s[i]))
set_s = list(set(s))
if len(set_s) != len(s):
    for i in set_s:
        if s.count(i) >= 2:
            count += int(s.count(i) * (s.count(i) - 1) / 2)
print(count)