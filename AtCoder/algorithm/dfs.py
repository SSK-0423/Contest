import sys
#入力処理
H,W = map(int,input().split())
#list()でリストを生成 list('abc') ['a','b','c']
table = [list(input()) for i in range(H)]

#地図の生成
masu = [[0 for i in range(H)] for j in range(W)]

for i in range(H):
    for j in range(W):
        if(table[i][j] == 's'):
            sx,sy = i,j
            break

#深さ優先探索
def search(x,y):
    #地図の外や壁の場合
    if(x < 0 or y < 0 or x >= H or y >= W or table[x][y] == '#'):
        return
    #すでに探索済みの場合
    if(H >= 2):
        if(masu[x][y]): return
    else:
        if(masu[x]): return
    #ゴールを見つけた
    if(table[x][y] == 'g'):
        print('Yes')
        sys.exit()

    masu[x][y] = 1
    
    search(x - 1,y) # 左
    search(x + 1,y) # 右
    search(x,y - 1) # 下
    search(x,y + 1) # 上
    
search(sx,sy)

print('No')