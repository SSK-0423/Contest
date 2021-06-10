S = list(input())
a = 0
for i in range(0,4):
    a += S.count(S[i])
if(a == 8):
    print('Yes')
else:
    print('No')