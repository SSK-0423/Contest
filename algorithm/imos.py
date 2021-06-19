i = int(input())
S = [0]*i
E = [0]*i
for j in range(0,i):
    S[j],E[j] = map(int,input().split())
'''入力終了'''

'''imos法'''
table = [0] * 10
#入店で+1 出店で-1
for j in range(0,i):
    table[S[j]] += 1
    table[E[j]] -= 1
#累積和を求める
for j in range(0,10):
    if(0 < j): table[j] += table[j - 1]
#最大値を求める
M = 0
for j in range(0,10):
    if(M < table[j]): M = table[j]

print(table)
print(M)