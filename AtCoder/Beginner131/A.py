s = int(input())
n = []
f = 0

while s > 0:
    n.append(s % 10)
    s = s // 10

n.reverse()
if(len(n) < 3):
    f = 1

for i in range(1,len(n)):
    if(n[i] == n[i -1]):
        f = 1
        break

if(f == 1):
    print('Bad')
else:
    print('Good')