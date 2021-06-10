a,b,c = map(int,input().split())
k = int(input())
num = [a,b,c]
while k > 0:
    num[num.index(max(num))] = max(num)*2
    k -= 1
print(sum(num))    