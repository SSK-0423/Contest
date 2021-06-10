w,h,n = map(int,input().split())
data = []
for i in range(n):
    data.append(list(map(int,input().split())))
map_data = [[0 for i in range(w)] for j in range(h)]
for i in range(n):
    if data[i][2] == 1:
       for j in range(h):
           for k in range(0,data[i][0]):
               map_data[j][k] = 1
    elif data[i][2] == 2:
       for j in range(h):
           for k in range(data[i][0],w):
               map_data[j][k] = 1
    elif data[i][2] == 3:
       for j in range(0,data[i][1]):
           for k in range(w):
               map_data[j][k] = 1
    else:
       for j in range(data[i][1],h):
           for k in range(w):
               map_data[j][k] = 1
ans = 0
for i in range(h):
    ans += map_data[i].count(0)
print(ans)