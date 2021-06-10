n = int(input())
s = []
for i in range(n):
    s.append(input())
m = int(input())
t = []
for i in range(m):
    t.append(input())
#内包表記で辞書を作成
#list(set(s))で重複を取り除いたlistを取得
num_s = {key: 0 for key in list(set(s))}
for i in num_s.keys():
    num_s[i] = s.count(i)
for i in num_s.keys():
    num_s[i] -= t.count(i)
#valueの値が最大となるkeyを取得
ans = max(num_s.values())
if ans < 0:
    print(0)
else:
    print(ans)