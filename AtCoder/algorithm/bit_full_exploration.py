money = 300
item = (('みかん',100),('りんご',200),('ぶどう',300))
n = len(item)
# n個の選択肢にYes or Noの2択が存在する
# 2^n
for i in range(2 ** n):
    bag = []
    total = 0
    for j in range(n):# nは2進数の桁数
        if((i >> j) & 1): # n桁目が1だった時
                          # (i >> n) & 1 でｎ桁目が1かどうかをチェック
            bag.append(item[j][0]) # item[j][0]で果物名を取り出す
            # j = 0 : みかん j = 1 : りんご j = 2 : ぶどう
            total += item[j][1] # 果物の値段を足す
    if(total <= money):
        print(total,bag)