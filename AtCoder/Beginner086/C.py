n = int(input())
t = [[0,0,0]]

for i in range(n):
    t.append(list(map(int,input().split())))

can = True

for i in range(n):
    #偶数奇数が毎回入れ替わる (1,1) (1,2)
    dt = t[i+1][0] - t[i][0]
    dist = abs(t[i+1][1] - t[i][1]) + abs(t[i+1][2] - t[i][2])
    if dt < dist:
        can = False
    if dt % 2 != dist % 2:
        can = False

if can:
    print('Yes')
else:
    print('No')