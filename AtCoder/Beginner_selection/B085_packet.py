#パケット法
n = int(input())
a = []
for i in range(0,n):
    a.append(int(input()))
    
num = [0]*110

for i in range(0,n):
    num.insert(i,a[i])
    
res = 0

for i in range(0,101):
    if(num[i] > 0):
        res += 1
        
print(res)