n,m = map(int,input().split())
city = []
num = [0] * n
for i in range(m):
    city.append(list(map(int,input().split())))
for i in range(m):
    for j in range(2):
            num[city[i][j] - 1] += 1
for i in num:
    print(i)