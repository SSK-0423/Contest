# from queue import LifoQueue ←遅い

# depueの方が高速なのでこちらを用いる
from collections import deque
#深さ優先探索
def dfs(start_y,start_x,map_list):
    s = deque()
    s.append([start_y,start_x])
    
    checked = [[0]*W for _ in range(H)]
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    while s:
        y,x = s.pop()

        if map_list[y][x] == 'g':
            return True

        # 探索候補
        for i in range(4):
            next_y = y + dy[i]
            next_x = x + dx[i]
            if next_y < 0 or next_x < 0 or next_y > H-1 or next_x > W-1 or map_list[next_y][next_x] == '#':
                continue
            # 未探索の時のみスタックに追加
            elif checked[next_y][next_x] == 0:
                checked[next_y][next_x] = 1
                s.append([next_y,next_x])

# 入力処理
H,W = map(int,input().split())
map_list = [input() for _ in range(H)]

for i in range(H):
    if map_list[i].find('s') != -1:
        start_y = i
        start_x = map_list[i].find('s')
        break

if dfs(start_y,start_x,map_list):
    print('Yes')
else:
    print('No')