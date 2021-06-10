import sys
#再帰の上限を設定（これをしないと再帰の回数上限を突破してRE）
sys.setrecursionlimit(10**6)
#入力処理
H,W = map(int,input().split())
DATA = [list(input()) for i in range(H)]
#マップの初期化
map_list = [[False for i in range(W)]for j in range(H)]
#マップ生成
for i in range(H):
    for j in range(W):
        if(DATA[i][j] == 's'):
            start_x = j
            start_y = i
            map_list[i][j] = 's'
        elif(DATA[i][j] == 'g'):
            map_list[i][j] = 'g'
        elif(DATA[i][j] == '.'):
            map_list[i][j] = True
#チェック済み配列を初期化
checked = [[0 for i in range(W)]for j in range(H)]
#探索
def search(y,x,checked):
    if x < 0 or y < 0 or x >= W or y >= H or map_list[y][x] == False : return
    if checked[y][x] == 1: return
    if map_list[y][x] == 'g':
        print('Yes')
        sys.exit()
    checked[y][x] = 1
    search(y + 1,x,checked)
    search(y - 1,x,checked)
    search(y,x + 1,checked)
    search(y,x - 1,checked)
search(start_y,start_x,checked)
print('No')