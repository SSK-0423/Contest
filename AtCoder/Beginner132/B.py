n = int(input())
p = list(map(int,input().split()))
count = 0
num = []

for i in range(1,n - 1):
    num.append(p[i-1])
    num.append(p[i])
    num.append(p[i+1])
    num.sort()
    if(num[1] == p[i]):
        count += 1
    num = []
print(count)