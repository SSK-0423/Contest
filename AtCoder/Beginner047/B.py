w,h,n = map(int,input().split())
data = []
for i in range(n):
    data.append(list(map(int,input().split())))
map_data = [[0 for i in range(w)] for j in range(h)]
for i in range(n):
    if data[i][2] == 1:
       for j in range(h):
           map_data[j][:data[i][0]] = [1]*data[i][0]
    if data[i][2] == 2:
       for j in range(h):
           map_data[j][data[i][0]:] = [1]*(w - data[i][0])
    if data[i][2] == 3:
       for j in range(h):
           map_data[:data[i][1]] = [1]*w
    if data[i][2] == 4:
       for j in range(h):
           map_data[data[i][1]:][:] = [1]*w
ans = 0
print(map_data)
for i in range(h):
    ans += map_data[i].count(0)
print(ans)