a = [1,6,3,8,4,2,9,5,7]
b = [0]
ans = 0
for i in range(0,len(a)):#a[1,6,3,8,4,2,9,5,7]
    b.append(a[i] + b[i])
for i in range(3,len(b)):#b=[0,1,7,10,18,22,24,33,38,45]
    ans = max(ans,b[i] - b[i-3])
print(ans)
