n = int(input())
w = list(map(int,input().split()))
s = 0
for i in range(n):
    s = s + w[i]
    
s1 = 0
s2 = 0
ans = 100 * 100

for i in range(n): #i[0,1,2]
    for j in range(0,i + 1):
        s1 += w[j]
        
    s2 = s - s1
    if(ans > abs(s1 -s2)):
        ans = abs(s1 - s2)
    s1 = 0
        
print(ans)
