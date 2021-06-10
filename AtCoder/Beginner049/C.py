s = input()
t = ''
divide = ['dream','dreamer','erase','eraser']
#後ろから見るために文字列を反転
s = s[::-1]
for i in range(4):
    divide[i] = divide[i][::-1]
i = 0
while i < len(s):
    ends = False
    for j in range(4):
        div_str = divide[j]
        if s[i:i+len(div_str)] == div_str:
            t += s[i:i+len(div_str)]
            i += len(div_str)
            break
        elif j == 3:
            ends = True
    if ends:
        break
if t == s:
    print('YES')
else:
    print('NO')