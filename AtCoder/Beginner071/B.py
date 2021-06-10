s = input()
packet = 'abcdefghijklmnopqrstuvwxyz'
checked = [0]*26
ans = []
for i in range(len(s)):
    checked[packet.index(s[i])] = 1
for i in range(26):
    if checked[i] != 1:
        ans.append(packet[i])
ans.sort()
if sum(checked) != 26:
    print(ans[0])
else:
    print('None')
    