n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
b = list(a)
a.sort(reverse=True)

max_num = max(a)
count = a.count(max_num)

for i in a:
    if i < max_num:
        max_num2 = i
        break

for i in range(n):
    if b[i] == max_num and count == 1:
        print(max_num2)
    else:
        print(max_num)
