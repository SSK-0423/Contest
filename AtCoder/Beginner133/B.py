import math

def cul(a,b,d):
    num = 0
    for i in range(d):
        num += (a[i] - b[i]) ** 2
    return math.sqrt(num)

N,D = map(int,input().split())
X = []
count = 0
d = 0
for i in range(N):
        X.append(list(map(int,input().split())))
for i in range(N):
    for j in range(i+1,N):
        if(i != j):
            d = cul(X[i],X[j],D)
            print(d - int(d))
        if (d - int(d)) == 0.0:
            count += 1

print(count)