n = int(input())
s = input()
x = 0
max_x = 0
for i in s:
    if i == "I":
        x += 1
    else:
        x -= 1
    if x > max_x:
        max_x = x
print(max_x)