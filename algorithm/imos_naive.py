i = int(input())
S = [0]*i
E = [0]*i
for j in range(0,i):
    S[j],E[j] = map(int,input().split())

table = [0]*10

for j in range(0,i):
    for k in range(S[j],E[j] + 1):
        table[k] += 1

M = 0
for j in range(0,10):
    if(M < table[j]): M = table[j]

print(table)
print(M)